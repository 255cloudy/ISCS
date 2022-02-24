import sqlite3


class Sqlite():

    def __init__(self, filepath):
        self.conn = None
        try:
            conn = sqlite3.connect(filepath)
        except(sqlite3.DatabaseError) as dbError:
            print(f"database error {dbError}")
        except(Exception) as error:
            print(f"an error occured {error}")
        finally:
            self.conn = conn
    
    def __del__(self):
        if self.conn:
            self.conn.close()
    
    def read(self, tablename, columns):
        col_string = ''
        for column in columns:
            col_string += f"{column}, "
        
        col_string = col_string[:-2]
        querystring = f" SELECT {col_string} FROM {tablename}"
        cur = self.conn.cursor()
        cur.execute(querystring)
        rows = cur.fetchall()
        return rows


def read_test():
    sqlDb = Sqlite('database.sqlite')
    print(sqlDb.read('country', ['id', 'name']))    
        
