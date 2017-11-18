# http://zetcode.com/db/sqlitepythontutorial/
# http://pythoncentral.io/advanced-sqlite-usage-in-python/
# https://www.tutorialspoint.com/sqlite/sqlite_data_types.htm
import sqlite3
import datetime

conn = None
# statments
database_ = "app/mod_db/database.db"
sql_create = "create table if not exists holder(id INTEGER PRIMARY KEY, note TEXT, topic TEXT, url TEXT, published NUMERIC)"
sql_insert = "insert into holder (id, note, topic, url, published) values (?, ?, ?, ?, ?)"
# print("\nSQLite3 project " + str(datetime.now()) + " data\n")

import logging
logger = logging.getLogger(__name__)

def get_database():
    global database_
    return database_

def init():
    msg = None
    try:
        global conn
        conn = sqlite3.connect(get_database())
        cur = conn.cursor()
        global sql_create
        cur.execute(sql_create)
        msg = "tab created if not existed"
        logger.info(msg)
    except sqlite3.OperationalError as e:
        msg = str(e)
    return msg

def dummy_data():
    """ doc """
    msg = None
    global conn
    try:
        conn = sqlite3.connect(get_database())
        with conn:
            cur = conn.cursor()
            timeNow = datetime.datetime.now()
            global sql_insert
            cur.execute(sql_insert, (1,"Test note","topic","www.bla.com", timeNow))
            conn.commit()
            msg = "added row"
    except sqlite3.OperationalError as e:
        print(e)
        conn.rollback()
    print(msg)








# print(init())
# dummy_data()
