#Get Combine Data from nflcombineresults.com
import urllib.request
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

def combine_data(position):
	headers = ['Player', 'College', 'Height', 'Weight', 'Hand_size', 'Arm_length', '40_time', 'Bench', 'Vert', 'Broad', 'Shuttle']
	df = pd.DataFrame(columns = headers)
	#columns for dataframe
	players = []
	college = []
	height = []
	weight = []
	hand_size = []
	arm_length = []
	forty_time = []
	bench = []
	vert = []
	broad = []
	shuttle = []
	df_years = []

	years =[]
	for i in range(1987,2018):
		years.append(i)

	for year in years:
		url = "http://nflcombineresults.com/nflcombinedata_expanded.php?year={}&pos={}&college=".format(year,position) 
		page = urllib.request.urlopen(url)
		soup = BeautifulSoup(page,"lxml")

		#qb stats tables - passing only
		table = soup.find("table", class_ = "sortable")
		table_body = soup.find("tbody")
		# table 1: min 50 passes (decreases to 40 passes in 1987) for WR, 25 passes for TE
		all_rows = table_body.find_all("tr")
		for row in all_rows:
			cells = row.find_all("td")
			players.append(cells[0].find(text = True))
			college.append(cells[1].find(text = True))
			height.append(cells[2].find(text = True))
			weight.append(cells[6].find(text = True))
			hand_size.append(cells[9].find(text = True))
			arm_length.append(cells[11].find(text = True))
			forty_time.append(cells[12].find(text = True))
			bench.append(cells[13].find(text = True))
			vert.append(cells[13].find(text = True))
			broad.append(cells[13].find(text = True))
			shuttle.append(cells[13].find(text = True))
			df_years.append(year)

	df['Player'] = players
	df['College'] = college
	df['Height'] = height 
	df['Weight'] = weight
	df['Arm_length'] = arm_length
	df['40_time'] = forty_time
	df['Bench'] = bench
	df['Vert'] = vert
	df['Broad'] = broad
	df['Shuttle'] = shuttle
	df['Year'] = df_years

	df.to_csv("{}_combine_data.csv".format(position))

combine_data("RB")
combine_data("QB")
combine_data("WR")
combine_data("TE")
