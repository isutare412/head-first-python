import mysql.connector
from pprint import pprint

dbconfig = {
    'host': '127.0.0.1',
    'user': 'vsearch',
    'password': 'vsearchpassword',
    'database': 'vsearchlogDB',
}

if __name__ == '__main__':
    dbconn = mysql.connector.connect(**dbconfig)
    dbcursor = dbconn.cursor()

    dbcursor.execute('DESCRIBE log')
    pprint(dbcursor.fetchall())

    dbcursor.close()
    dbconn.close()
