import sqlite3

conn = sqlite3.connect('content.sqlite')
cur = conn.cursor()

cur.execute('''DROP TABLE IF EXISTS LegendStage''')

cur.execute('''CREATE TABLE IF NOT EXISTS LegendStage
    (id INTEGER UNIQUE, urlsuf TEXT UNIQUE, stageName TEXT, Content TEXT)''')

cur.execute('''select max(id) from Stages''')
maxid = cur.fetchone()
maxid = maxid[0]

for i in range(maxid):
    id = i+1
    #print(id)
    cur.execute('''select * from Stages WHERE id=?''', (id,))
    tmp = cur.fetchone()
    urlsuf = tmp[1]
    stageName = tmp[2]

    if urlsuf.find('-') == -1 or urlsuf.startswith('s000') == False:
        continue
    #print(id)
    #print(urlsuf)
    #print(stageName)
    cur.execute('''INSERT OR IGNORE INTO LegendStage (id, urlsuf, stageName)
    VALUES (?,?,?) ''',(id,urlsuf,stageName))

conn.commit()
cur.close
