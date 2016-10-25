#-*- coding:utf-8 -*-
import requests
import psycopg2
import json

#from views import get

from bs4 import BeautifulSoup as BS

conn = psycopg2.connect("dbname=test user=student")

cur = conn.cursor()

cur.execute("CREATE TABLE test (id serial PRIMARY KEY, lon int, lat int, address varchar);")

atm = requests.get('http://catalog.api.2gis.ru/search?what=kaspi&where=Almaty&version=1.3&key=ruczoy1743&')
atm.json()


parsed_atm = json.loads(atm.text)
# print parsed_atm
# print url
# user_agent = {'ser-agent': 'Mozilla/5.0'}
# html = requests.get(url, verify = False).text
# soup = BS(html,'html.parser')
for b in parsed_atm["result"]:
	print b["lon"] + " " + b["lat"] + " " + b["address"]
	cur.execute("INSERT INTO test (lon, lat, address) VALUES (%s, %s, %s)", (b["lon"], b["lat"], b["address"]))
conn.commit()
# cur.execute("SELECT * FROM test;")
# cur.fetchone()
#text = soup.find(id='ip')
# #print (text.span.text)
# for b in soup.find_all('b', text='lon'):
#     div = b.parent.findNext('div')

#     labName = div.b.a.contents[0]
#     print(labName)
    
         
