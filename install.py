import sqlite3

con = sqlite3.connect('todo.db')
cur = con.cursor()
try:
    cur.execute('select * from task')
    print "Already installed."
except:
    cur.execute('CREATE TABLE task (task_id INTEGER PRIMARY KEY, detail VARCHAR(200), added varchar(25), due_date VARCHAR(25), is_done INTEGER, is_deleted INTEGER)')
    con.commit()
    "Installed successfully"
