import sqlite3

class Database:
    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()

    def get_koll(self):
        with self.connection:
            result = self.cursor.execute("SELECT * FROM  Users ").fetchall()
            return result

    def _add_user(self,qury,data):
        with self.connection:
            self.




