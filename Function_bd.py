import sqlite3
import re
class Database:
    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()

    def get_koll(self):
        with self.connection:
            result = self.cursor.execute("SELECT * FROM  Users ").fetchall()
            return result

    def add_user(self,user_id,user_name,priveleg='start'):
        with self.connection:
            try:
                data = self.cursor.execute('SELECT username FROM Users WHERE user_id=?',(user_id,))
                if data.fetchall()[0] == user_name :
                    return
            except:
                self.cursor.execute('INSERT INTO Users(user_id,username,privileg,Content_id) VALUES (?,?,?,?) ',
                                    (user_id, user_name, priveleg, user_id))
                self.cursor.execute('INSERT INTO Content(CONTENT_ID) VALUES (?)',(user_id,))


    def _extract_num_(self,string):
        digits = re.findall(r'\d+', string)
        return ''.join(digits)


    def add_my_groups(self,Udata,user_id):
        Udata = self._extract_num_(Udata)
        with self.connection:
            #data = self.cursor.execute('SELECT my_groum FROM Users WHERE user_id=?',(user_id,)).fetchone()
            privileg = self.cursor.execute('SELECT privileg FROM Users WHERE user_id=?',(user_id,)).fetchone()
            print(type(privileg[0]))
            match privileg[0]:
                case "start":
                    self.cursor.execute('UPDATE Users SET my_groum=? WHERE user_id=?' ,(Udata,user_id,))
                case "Middle":
                    pass
                case "Full":
                    pass









