import sqlite3
import re
from bs4 import BeautifulSoup

conn = sqlite3.connect('content.sqlite')
cur = conn.cursor()

cur.execute('drop table if exists LegStageDetail')

cur.execute('''CREATE TABLE IF NOT EXISTS LegStageDetail
    (id INTEGER UNIQUE, urlsuf TEXT UNIQUE, stageName TEXT, enemyNum INTEGER, ParentStage INTEGER)''')

cur.execute('select max(id) from LegendStage')
idrow = cur.fetchone()
idmax = idrow[0]
#idmax = 4

for id in range(1,idmax+1):
    cur.execute('''select * from LegendStage where id=?''', (id,))
    row = cur.fetchone()
    if row is None:
        continue
    #cur.execute('''select * from LegStageDetail where id=?''',(id,))
    #row2 = cur.fetchone()
    #if row2 is not None:
    #    continue

    id = row[0]
    urlsuf = row[1]
    SN = row[2]
    content = row[3]
    soup = BeautifulSoup(content,'html.parser')
    tags = soup('a')
    ## Find Parent Stage id
    ParentStage = urlsuf
    ppos = urlsuf.find('s')
    ppos2 = urlsuf.find('-')
    parentStage = urlsuf[ppos+1:ppos2]
    PS = int(parentStage)

    enemyNum = 0
    for tag in tags:
        text = str(tag)
        if text.find('/enemy/') == -1 or text.find('?mag=') ==-1:
            continue

        #print(id, text, enemyNum)
        pos = text.find('">')
        pos2 = text.find('</')
        EnemyName = text[pos+2:pos2]
        enemyNum = enemyNum + 1
    type(enemyNum)
    type(PS)
    print(enemyNum,PS)
    cur.execute('''INSERT OR IGNORE INTO LegStageDetail (id, urlsuf, stageName, enemyNum, ParentStage)
            VALUES (?,?,?,?,?) ''',(id,urlsuf,SN,enemyNum, PS))

conn.commit()
cur.close


#s00000-01.html
