import sqlite3
import time
import ssl
import urllib.request, urllib.parse, urllib.error
from urllib.parse import urljoin
from urllib.parse import urlparse
import re
from datetime import datetime, timedelta
from bs4 import BeautifulSoup

urlbase = 'https://battlecats-db.com/stage/'
#url = "https://battlecats-db.com/stage/index_legendstory.html"

conn = sqlite3.connect('content.sqlite')
cur = conn.cursor()

cur.execute('''SELECT max(id) from LegendStage''')
row = cur.fetchone()
idmax = row[0]
#idmax = 3

for id in range(1,idmax+1):
    cur.execute('''select * from LegendStage where id = ?''',(id,))
    row = cur.fetchone()
    if row is None:
        continue
    #print(id)
    #print(row)

    urlsuf = row[1]
    SN = row[2]
    tmp = row[3]
    if tmp is not None:
        continue
    #print(SN)
    url = urlbase + urlsuf

    uh = urllib.request.urlopen(url)
    text = uh.read().decode()
    if uh.getcode() != 200 :
        print("Error code=",uh.getcode(), url)
        print(url,len(text))
        continue
    if id == 2:
        file = open("temp.txt",'w')
        file.write(text)
    #print(text)
    print(id, urlsuf, SN)
    cur.execute('''INSERT OR REPLACE INTO LegendStage (id, urlsuf, stageName, Content)
        VALUES (?,?,?,?) ''',(id, urlsuf, SN, text))

#cur.execute('''INSERT OR REPLACE INTO LegendStage (id, urlsuf, Content) VALUES (?,?,?) ''', (id, urlsuf, text))

conn.commit()
cur.close
