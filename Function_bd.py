import re
import sqlite3


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
                if data.fetchall()[0] == user_name:
                    return
            except:
                self.cursor.execute('INSERT INTO Users(user_id,username,privileg,Content_id) VALUES (?,?,?,?) ',
                                    (user_id, user_name, priveleg, user_id))
                self.cursor.execute('INSERT INTO Content(CONTENT_ID) VALUES (?)',(user_id,))


    def __extract_num_(self,string):
        digits = re.findall(r'\d+', string)
        return ''.join(digits)



    def add_my_groups(self,Udata,user_id):
        with self.connection:
            # data = self.cursor.execute('SELECT my_groum FROM Users WHERE user_id=?',(user_id,)).fetchone()
            privileg = self.cursor.execute('SELECT privileg from Users where user_id = ?',(user_id,)).fetchmany()
            match privileg[0][0]:
                case 'start':
                    self.cursor.execute(f'update Users set my_groum = {Udata} where user_id =?',(user_id,))
                case 'Seniur':
                     self.cursor.execute(f'update Users set my_groum = {Udata} where user_id =?', (user_id,))


    def add_Pars_groups(self, Udata, user_id):
        with self.connection:

                # data = self.cursor.execute('SELECT my_groum FROM Users WHERE user_id=?',(user_id,)).fetchone()
                privileg = self.cursor.execute('SELECT privileg FROM Users WHERE user_id=?', (user_id,)).fetchmany()

                match privileg[0][0]:
                    case 'start':
                        self.cursor.execute('UPDATE Content SET Group_id=? WHERE Content_id=?', (Udata, user_id,))
                    case 'Middle':

                        self.cursor.execute('UPDATE Content SET Group_id=? WHERE Content_id=?', (Udata, user_id,))
                    case 'Seniur':

                        self.cursor.execute('UPDATE Content SET Group_id=? WHERE Content_id=?', (Udata, user_id,))




    def send_query(self,data,query):
        with self.connection:
            data = self.cursor.execute(query,(data,))
            if data == None:
             data = eval(data)
             return data



    def send_defult_query(self,data,query):
        with self.connection:
            data = self.cursor.execute(query, (data,)).fetchone()
            return data




    def apdate_data(self,table,column,indef_column,data,user_id):
        with self.connection:
            self.cursor.execute(f'UPDATE {table} SET {column}=? WHERE {indef_column}=? ',(data,user_id,))



# if __name__ == "__main__":
#     db = Database(db_file='db.sqlite')
#     print(db.send_defult_query(query='SELECT privileg FROM Users WHERE user_id=?',data=1365677446).fetchone())