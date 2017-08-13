import requests
from bs4 import BeautifulSoup

r=requests.get("http://xpau.se/")
soup=BeautifulSoup(r.text,"lxml")
movie=soup.find_all("table",class_="topic_table")

shows={}

for i in movie:
	shows[i.a["href"]]={}

for i in movie:
	shows[i.a["href"]]["name"]=i.a.get_text()

for i in movie:
	shows[i.a["href"]]["desc"]=i.pre.get_text()

for i in movie:
	shows[i.a["href"]]["link"]=i.a["href"]

#for i in movie:
#	print("Name: " + shows[i.a["href"]]["name"] + "\n" + "Link: " + shows[i.a["href"]]["link"] + "\n" + "Description: \n" + shows[i.a["href"]]["desc"] + "\n\n\n")	

for i in movie:
	print("Name: " + shows[i.a["href"]]["name"] + "\n")