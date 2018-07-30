# Get Birthdays For All* Players
#* Birthdays not available for some players- will see what to do with that

import urllib.request
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

def get_birthdays(position):
	if position != "rb":
		df = pd.read_csv("{}data.csv".format(position))
	else:
		df = pd.read_csv("rbdata_rush.csv".format(position))

	#Get list of players at position, years, create list for already visited players
	players = df['Player'].unique()
	years = list(range(1986,2018))
	visited = []
	bdays = []


	for year in years:
		url = "https://www.footballoutsiders.com/stats/{}{}".format(position,year) 
		page = urllib.request.urlopen(url)
		soup = BeautifulSoup(page,"lxml")

		tables = soup.find_all("table", class_ = "stats")
		count  = 0
		for table in tables:
			count += 1
			rows = table.find_all("tr")
			for row in rows:
				cells = row.find_all("td")
				
				#if row full of headers, skip, else extract data from row
				if str(cells[0].find(text = True)) == "Player":
					continue
				else:
					name = cells[0].find(text = True)
					#if player not already visited, go to player bio (if available)
					if name not in visited:
						link = cells[0].find("a", href = True)
						visited.append(name)
						if link is not None:
							try:
								p_url = 'https://www.footballoutsiders.com{}'.format(link['href'])
								p_page = urllib.request.urlopen(p_url)
								p_soup = BeautifulSoup(p_page,"lxml")
								#player info
								info = p_soup.find("div", class_ = "left")
								if info is not None:
									cells = info.find_all("p")
									#find birthday info, get birthdate
									for cell in cells:
										if cell.find(text = True) == 'Birthdate: ':
											bdays.append(cell.find_all(text = True)[1])
								else:
									bdays.append(np.nan)
							except Exception as e:
								print(e)
								print("Player: ",name)
								print("URL: ",p_url)
								bdays.append(np.nan)

						else:
							bdays.append(np.nan)


	birthday_df = pd.DataFrame({"Player: ":visited,"Birthdate: ":bdays })
	birthday_df.to_csv("../Data/{}bdays.csv".format(position))

get_birthdays("qb")
get_birthdays("wr")
get_birthdays("te")
get_birthdays("rb")




