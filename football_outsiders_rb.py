import urllib.request
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

#rushing data frame
headers = ['Player', 'Team', 'DYAR', 'DVOA', 'Rushes', 'EYds', 'TD', 'Suc_rate', 'Year']
df_rush = pd.DataFrame(columns = headers)
#columns for dataframe
players = []
team = []
dyar = []
dvoa = []
rushes = []
eyards = []
td = []
suc_pct = []
df_years = []

#receiving data frame
headers_2 = ['Player', 'Team', 'DYAR_receiving', 'DVOA_receiving', 'EYds_receiving', 'TD_receiving', 'Catch_rate', 'Year']
df_rec = pd.DataFrame(columns = headers_2)
#columns for dataframe
players_2 = []
team_2 = []
dyar_2 = []
dvoa_2 = []
eyards_2 = []
td_2 = []
catch_pct = []
df_years_2 = []

#years we are collecting data for
years = []
for i in range(1986,2018):
	years.append(i)

for year in years:
	#collecting football outsiders run data
	url = "https://www.footballoutsiders.com/stats/rb{}".format(year) 
	page = urllib.request.urlopen(url)
	soup = BeautifulSoup(page,"lxml")

	#rb stats tables - first two are rushing, second two are receiving
	rb_tables = soup.find_all("table", class_ = "stats")

	for counter, table in enumerate(rb_tables, 1):
		#rushing stats
		if counter == 1:
			#first table: min 100 rushes
			all_rows_1 = table.find_all("tr")
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
					rushes.append(cells[9].find(text = True))
					eyards.append(cells[11].find(text = True))
					td.append(cells[12].find(text = True))
					suc_pct.append(cells[14].find(text = True))
					df_years.append(year)
		elif counter == 2:
			#second table: 10-99 rushes
			all_rows_1 = table.find_all("tr")
			for row in all_rows_1:
				cells = row.find_all("td")
				#if row full of headers, skip, else extract data from row
				if str(cells[0].find(text = True)) == "Player":
					continue
				else:
					players.append(cells[0].find(text = True))
					team.append(cells[1].find(text = True))
					dyar.append(cells[2].find(text = True))
					dvoa.append(cells[4].find(text = True))
					rushes.append(cells[6].find(text = True))
					eyards.append(cells[8].find(text = True))
					td.append(cells[9].find(text = True))
					suc_pct.append(np.nan)
					df_years.append(year)
		#receiving stats
		elif counter == 3:
			#third table: min 25 passes
			all_rows_1 = table.find_all("tr")
			for row in all_rows_1:
				cells = row.find_all("td")
				#if row full of headers, skip, else extract data from row
				if str(cells[0].find(text = True)) == "Player":
					continue
				else:
					players_2.append(cells[0].find(text = True))
					team_2.append(cells[1].find(text = True))
					dyar_2.append(cells[2].find(text = True))
					dvoa_2.append(cells[6].find(text = True))
					eyards_2.append(cells[11].find(text = True))
					td_2.append(cells[12].find(text = True))
					catch_pct.append(cells[13].find(text = True))
					df_years_2.append(year)

		elif counter == 4:
			#fourth table: 10-24 passes
			all_rows_1 = table.find_all("tr")
			for row in all_rows_1:
				cells = row.find_all("td")
				#if row full of headers, skip, else extract data from row
				if str(cells[0].find(text = True)) == "Player":
					continue
				else:
					players_2.append(cells[0].find(text = True))
					team_2.append(cells[1].find(text = True))
					dyar_2.append(cells[2].find(text = True))
					dvoa_2.append(cells[4].find(text = True))
					eyards_2.append(cells[8].find(text = True))
					td_2.append(cells[9].find(text = True))
					catch_pct.append(cells[10].find(text = True))
					df_years_2.append(year)


df_rush["Player"] = players
df_rush["Team"] = team
df_rush["DYAR"] = dyar
df_rush["DVOA"] = dvoa
df_rush["Rushes"] = rushes
df_rush["EYds"] = eyards
df_rush["TD"] = td
df_rush["Suc_rate"] = suc_pct
df_rush["Year"] = df_years


df_rec["Player"] = players_2
df_rec["Team"] = team_2
df_rec["DYAR_receiving"] = dyar_2
df_rec["DVOA_receiving"] = dvoa_2
df_rec["EYds_receiving"] = eyards_2
df_rec["TD_receiving"] = td_2
df_rec["Catch_rate"] = catch_pct
df_rec["Year"] = df_years_2

df_rush.to_csv('rbdata_rush.csv')
df_rec.to_csv('rbdata_rec.csv')

