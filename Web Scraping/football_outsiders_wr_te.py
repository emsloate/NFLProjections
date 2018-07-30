# Get wide receiver data from Football Outsiders
import urllib.request
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np


def receiving_data(position):
	headers = ['Player', 'Team', 'DYAR', 'DVOA', 'Targets', 'Yds', 'EfYds', 'TD', 'Catch_rate', 'Year']
	df = pd.DataFrame(columns = headers)
	#columns for dataframe
	players = []
	team = []
	dyar = []
	dvoa = []
	passes = []
	yards = []
	eyards = []
	td = []
	catch_pct = []
	df_years = []

	years =[]
	for i in range(1986,2018):
		years.append(i)


	for year in years:
		url = "https://www.footballoutsiders.com/stats/{}{}".format(position,year) 
		page = urllib.request.urlopen(url)
		soup = BeautifulSoup(page,"lxml")

		#qb stats tables - passing only
		tables = soup.find_all("table", class_ = "stats")
		
		# table 1: min 50 passes (decreases to 40 passes in 1987) for WR, 25 passes for TE
		all_rows_1 = tables[0].find_all("tr")
		for row in all_rows_1:
			cells = row.find_all("td")

			#if row full of headers, skip, else extract data from row
			if str(cells[0].find(text = True)) == "Player":
				continue
			else:
				players.append(cells[0].find(text = True))
				team.append(cells[1].find(text = True))
				dyar.append(cells[2].find(text = True))
				dvoa.append(cells[6].find(text = True))
				passes.append(cells[9].find(text = True))
				yards.append(cells[10].find(text = True))
				eyards.append(cells[11].find(text = True))
				td.append(cells[12].find(text = True))
				catch_pct.append(cells[13].find(text = True))
				df_years.append(year)

		#table 2: 10-49 passes, 10-24 Passes
		all_rows_2 = tables[1].find_all("tr")
		for row in all_rows_2:
			cells = row.find_all("td")
			if str(cells[0].find(text = True)) == "Player":
				continue
			else:
				players.append(cells[0].find(text = True))
				team.append(cells[1].find(text = True))
				dyar.append(cells[2].find(text = True))
				dvoa.append(cells[4].find(text = True))
				passes.append(cells[6].find(text = True))
				yards.append(cells[7].find(text = True))
				eyards.append(cells[8].find(text = True))
				td.append(cells[9].find(text = True))
				catch_pct.append(cells[10].find(text = True))
				df_years.append(year)


	df["Player"] = players
	df["Team"] = team
	df["DYAR"] = dyar
	df["DVOA"] = dvoa
	df["Targets"] = passes
	df["Yds"] = yards
	df["EfYds"] = eyards
	df["TD"] = td
	df["Catch_rate"] = catch_pct
	df["Year"] = df_years


	df.to_csv('{}data.csv'.format(position))

receiving_data("../Data/wr")
receiving_data("../Data/te")