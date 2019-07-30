import sqlite3
import time
import ssl
import urllib.request, urllib.parse, urllib.error
from urllib.parse import urljoin
from urllib.parse import urlparse
import re
from datetime import datetime, timedelta
from bs4 import BeautifulSoup

url = "https://battlecats-db.com/stage/index_legendstory.html"

uh = urllib.request.urlopen(url)
text = uh.read().decode()
if uh.getcode() != 200 :
    print("Error code=",uh.getcode(), url)
print(url,len(text))
file = open("temp.txt",'w')
file.write(text)

conn = sqlite3.connect('content.sqlite')
cur = conn.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS Pages
    (id INTEGER UNIQUE, content TEXT)''')

cur.execute('''SELECT max(id) from Pages''')
try:
    row = cur.fetchone()
    if row is None:
        idnum = 0
    else:
        idnum = row[0]
except:
    idnum = 1
    idnum = idnum+1
cur.execute('''INSERT OR IGNORE INTO Pages  (id, content)
    VALUES ( ?, ? )''', ( idnum, text))



conn.commit()
cur.close
