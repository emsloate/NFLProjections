# Get expected values for draft picks from footballpersepective.com
import urllib.request
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np


url = 'http://www.footballperspective.com/draft-value-chart/'
page = urllib.request.urlopen(url)
soup = BeautifulSoup(page,"lxml")

table = soup.find("table", class_ = "tablepress tablepress-id-276")
table_body = table.find("tbody")
rows = table_body.find_all("tr")

picks = []
ev = []

#rows: draft pick, ev, nfl ev(not true ev)
for row in rows:
	cells = row.find_all("td")
	picks.append( int(cells[0].find(text = True)) )
	ev.append( float(cells[1].find(text = True)) )

df = pd.DataFrame({"Pick":picks,"EV":ev}, index = picks)

df.to_csv("draftevs.csv")