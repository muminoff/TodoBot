import sqlite3
from datetime import datetime
from time import strftime
class ToDo():
    message = ""
    def __init__(self, message):
        self.message = message
        parts = self.message.split(' ')
        self.command = parts[0]
        self.other_data = self.message[len(self.command)+1:]
        self.con = sqlite3.connect('todo.db')
        self.cur = self.con.cursor() 
    def add(self, task):
        now = datetime.now()
        query =  'INSERT INTO task (detail, added, is_done, is_deleted)' 
        query += ' values("%s", "%s", 0, 0)' % (task, now.strftime("%Y-%m-%d %H:%M:%S"))
        print query
        self.cur.execute(query)
        self.con.commit()
        print "added: " + str(task)
        return "Added!"
    def list(self):
        query = "SELECT task_id, detail, is_done FROM task"
        self.cur.execute(query)
        tasks = self.cur.fetchall()
        result = ""
        for task in tasks:
            result += str(task[0])
            result += " "
            result += '['
            result += task[1]
            result += ']'
            if task[2] == 1:
                result += " [+] "
            elif task[2] == 0:
                result += " [P]"
            result += '\n'
        return result
    def delete(self, id):
        query = "DELETE FROM task where task_id=%s" % id
        self.cur.execute(query)
        self.con.commit()
        return "Deleted!"
    def execute(self):
        if self.command == "add":
            return self.add(self.other_data) 
        elif self.command == "list":
            return self.list()
        elif self.command == "del":
            id = self.other_data.split(' ')[0]
            return self.delete(id)

