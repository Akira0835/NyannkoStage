import sqlite3
import ssl
import urllib.request, urllib.parse, urllib.error
from urllib.parse import urljoin
from urllib.parse import urlparse
import re
from bs4 import BeautifulSoup

stageurl = "https://battlecats-db.com/stage/index_legendstory.html"

urlbase = 'https://battlecats-db.com/stage/'

conn = sqlite3.connect('content.sqlite')
cur = conn.cursor()



cur.execute('''CREATE TABLE IF NOT EXISTS Stages
    (id INTEGER UNIQUE, urlsuf TEXT UNIQUE, stageName TEXT)''')

cur.execute('''select content from Pages''')
rowtext = cur.fetchone()
rowtext = rowtext[0]

soup = BeautifulSoup(rowtext,'html.parser')
tags = soup('a')

for tag in tags:
    urlsuf = tag.get('href',None)
    text = str(tag)
    isstage = urlsuf.startswith('s')    # Stage url have to start with s
    isnostar = text.find('?')          # if this is not star one stage, it contain ?
    pos = text.find('">')
    pos2 = text.find('</')
    stageName = text[pos+2:pos2]
    if isstage == True and isnostar == -1:
        cur.execute('''select max(id) from Stages''')
        id = cur.fetchone()
        id = id[0]
        if id is None:
            id = 0
        id = id + 1
        cur.execute('''INSERT OR IGNORE INTO Stages (id, urlsuf, stageName)
        VALUES (?,?,?) ''',(id,urlsuf,stageName))

conn.commit()
cur.close


#s00000-01.html
