import sqlite3

con = sqlite3.connect('todo.db')
cur = con.cursor()

cur.execute('SELECT * FROM task')
a = cur.fetchall()
for i in a:
    print i
