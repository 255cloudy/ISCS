from configparser import ConfigParser
import psycopg2

class Postgres():

    def __init__(self, inifile='database.ini', section_name='postgresql'):
        self.conn = None
         # create a parser
        parser = ConfigParser()

        # read config file
        parser.read(inifile)

        # get section, default to postgresql
        db_config = {}
        if parser.has_section(section_name):
            params = parser.items(section_name)
            for param in params:
                db_config[param[0]] = param[1]
        else:
            raise Exception('Section {0} not found in the {1} file'.format(section_name, inifile))
        conn = None
        try:
            conn = psycopg2.connect(**db_config)
                # create a cursor
            cur = conn.cursor()
        
	        # execute a statement
            print('PostgreSQL database version:')
            cur.execute('SELECT version()')

            # display the PostgreSQL database server version
            db_version = cur.fetchone()
            print(db_version)
       
	        # close the communication with the PostgreSQL
            cur.close()
        except(Exception, psycopg2.DatabaseError) as error:
            print(f"connection to database failed with error: {error}")
        
        finally:
            if conn:
                self.conn = conn

    def __del__(self):
        """ a destructor function to close the connections """
        if self.conn:
            self.conn.close()
            print("database connection closed")

    def create(self, tablename, columns, values):
        
        cur = self.conn.cursor()
        col_string= ""
        val_string=""
        col_string += "( "
        val_string += "( "
        for col in columns:
            col_string += f"{col}, "
            val_string += f"%s, "
            print(col_string)
        col_string = col_string[:-2] + " )"
        val_string = val_string[:-2] + " )"
        querystring = f"""INSERT INTO {tablename} {col_string} VALUES {val_string}"""
        print(querystring)
        cur.execute(querystring, values)
        self.conn.commit()
        cur.close()



def test_create():
    db = Postgres(inifile='testDB.ini')

    cols = [
        "username", "password", "email", 
    ]
    values = [
        "rucha2", "rucha", "colloruch2a@mail.com"
    ]
    db.create("accounts", cols, values)


