import sqlite3


conn = sqlite3.connect('content.sqlite')
cur = conn.cursor()

ParentStage = input('Input ParentStage NUmber: ')
EnemyNum = input('Input EnemyNumber: ')

ParentStage = int(ParentStage)
EnemyNum = int(EnemyNum)

cur.execute('''select stageName from LegStageDetail
    where ParentStage=? and enemyNum =?''',(ParentStage,EnemyNum))
row = cur.fetchall()

for SNtuple in row:
    SN = SNtuple[0]
    print(SN)
