import pymysql
conn=pymysql.connect(host='localhost', 
                     user='Bhoomika',
                     password='bhoomi@0626')
print('connected')
cur=conn.cursor()
cur.execute('use day1')
cur.execute('show tables')
tables=cur.fetchall()
for x in tables:
    print(x)