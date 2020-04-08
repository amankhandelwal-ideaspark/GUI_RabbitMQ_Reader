import os
import sqlite3

class DataSetup:
    def __init__(self):
        try:
            os.makedirs('data')
        except FileExistsError:
            print('directory exist')
        self.con = sqlite3.connect("data/local.db")

    def getDbCon(self):
        return self.con