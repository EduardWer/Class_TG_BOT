import sqlite3
import aiosqlite
class BD_helper:
    def __init__(self,datadase):
        self.database = datadase
        self.connect = aiosqlite.connect(self.database)
