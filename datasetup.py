import os
import sqlite3

class DataSetup:
    def __init__(self):
        try:
            os.makedirs('data')
        except FileExistsError:
            print('directory exist')
        self.con = sqlite3.connect("data/local.db")
        with open('sql/queue_details.sql') as f:
            q = f.read()
        cur = self.con.cursor()
        q = q.split(";")
        for query in q:
            try:
                cur.execute(query)
            except:
                print(query, ' Cannot be executed')

    def getDbCon(self):
        return self.con