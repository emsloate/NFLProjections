import urllib.request
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

headers = ['Player', 'Team', 'DYAR', 'DVOA', 'QBR', 'Passes','EYds', 'TD', 'INT', 'C%', 'Year']
df = pd.DataFrame(columns = headers)
#columns for dataframe
players = []
team = []
dyar = []
dvoa = []
qbr = []
passes = []
eyards = []
td = []
ints = []
comp_pct = []
df_years = []

#years we are collecting data for
years = []

#no QBR for these years ?????
for i in range(1986,2018):
	years.append(i)

for year in years:
	url = "https://www.footballoutsiders.com/stats/qb{}".format(year) 
	page = urllib.request.urlopen(url)
	soup = BeautifulSoup(page,"lxml")

	#qb stats tables - passing only
	tables = soup.find_all("table", class_ = "stats")
	
	# table 1: min 200 passes
	all_rows_1 = tables[0].find_all("tr")
	for row in all_rows_1:
		cells = row.find_all("td")

		#if row full of headers, skip, else extract data from row
		#qbr data only available for years >= 2008
		if str(cells[0].find(text = True)) == "Player":
			continue
		elif year <= 2007:
			players.append(cells[0].find(text = True))
			team.append(cells[1].find(text = True))
			dyar.append(cells[2].find(text = True))
			dvoa.append(cells[6].find(text = True))
			passes.append(cells[9].find(text = True))
			eyards.append(cells[11].find(text = True))
			td.append(cells[12].find(text = True))
			ints.append(cells[15].find(text = True))
			comp_pct.append(cells[16].find(text = True))
			qbr.append(np.nan)
			df_years.append(year)
		else:
			players.append(cells[0].find(text = True))
			team.append(cells[1].find(text = True))
			dyar.append(cells[2].find(text = True))
			dvoa.append(cells[6].find(text = True))
			qbr.append(cells[9].find(text = True))
			passes.append(cells[11].find(text = True))
			eyards.append(cells[13].find(text = True))
			td.append(cells[14].find(text = True))
			ints.append(cells[17].find(text = True))
			comp_pct.append(cells[18].find(text = True))
			df_years.append(year)

	#table 2: 10-199 passes
	all_rows_2 = tables[1].find_all("tr")
	for row in all_rows_2:
		cells = row.find_all("td")
		if str(cells[0].find(text = True)) == "Player":
			continue
		elif year <= 2007:
			players.append(cells[0].find(text = True))
			team.append(cells[1].find(text = True))
			dyar.append(cells[2].find(text = True))
			dvoa.append(cells[4].find(text = True))
			qbr.append(np.nan)
			passes.append(cells[6].find(text = True))
			eyards.append(cells[8].find(text = True))
			td.append(cells[9].find(text = True))
			ints.append(cells[12].find(text = True))
			comp_pct.append(cells[13].find(text = True))
			df_years.append(year)
		else:
			players.append(cells[0].find(text = True))
			team.append(cells[1].find(text = True))
			dyar.append(cells[2].find(text = True))
			dvoa.append(cells[4].find(text = True))
			qbr.append(cells[6].find(text = True))
			passes.append(cells[7].find(text = True))
			eyards.append(cells[9].find(text = True))
			td.append(cells[10].find(text = True))
			ints.append(cells[13].find(text = True))
			comp_pct.append(cells[14].find(text = True))
			df_years.append(year)
	

df["Player"] = players
df["Team"] = team
df["DYAR"] = dyar
df["DVOA"] = dvoa
df["Passes"] = passes
df["EYds"] = eyards
df["QBR"] = qbr
df["TD"] = td
df["INT"] = ints
df["C%"] = comp_pct
df["Year"] = df_years


df.to_csv('qbdata.csv')
		


