# http://zetcode.com/db/sqlitepythontutorial/
# http://pythoncentral.io/advanced-sqlite-usage-in-python/
# https://www.tutorialspoint.com/sqlite/sqlite_data_types.htm
import sqlite3
from datetime import date, datetime

conn = None
# statments
sql_create = "create table if not exists holder(id INTEGER PRIMARY KEY, note TEXT, published NUMERIC)"
sql_insert = "insert into holder (id, note, published) values (?, ?, ?)"
sql_select_all = "select * from holder"

# 
# print("\nSQLite3 project " + str(datetime.now()) + " data\n")

def init():
    msg = None
    try:
        global conn
        conn = sqlite3.connect("database.db")
        cur = conn.cursor()
        global sql_create
        cur.execute(sql_create)
        msg = "tab created if not existed"
    except sqlite3.OperationalError as e:
        msg = str(e)
    return msg

def dummy_data():
    msg = None
    global conn
    try:
        conn = conn = sqlite3.connect("database.db")
        with conn:
            cur = conn.cursor()
            timeNow = datetime.now()
            global sql_insert
            cur.execute(sql_insert, (2,"Test note", timeNow))
            conn.commit()
            msg = "added row"
    except sqlite3.OperationalError as e:
        print(e)
        conn.rollback()
    print(msg)







init()
# dummy_data()
