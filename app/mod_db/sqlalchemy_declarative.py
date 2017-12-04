# http://zetcode.com/db/sqlitepythontutorial/
# http://pythoncentral.io/advanced-sqlite-usage-in-python/
# https://www.tutorialspoint.com/sqlite/sqlite_data_types.htm
import sqlite3
import datetime

conn = None
# statments
database_ = "app/mod_db/database.db"
sql_create_holder = "create table if not exists holder(id INTEGER PRIMARY KEY autoincrement, note TEXT, topic TEXT, url TEXT, published NUMERIC)"
sql_insert_holder = "insert into holder (id, note, topic, url, published) values (?, ?, ?, ?, ?)"
# print("\nSQLite3 project " + str(datetime.now()) + " data\n")

sql_create_users = "create table if not exists users(id INTEGER PRIMARY KEY autoincrement, usern TEXT NOT NULL, passw TEXT NOT NULL)"
sql_insert_user = "insert into users (usern, passw) values (?, ?)"


import logging
logger = logging.getLogger(__name__)

def get_database():
    global database_
    return database_

def init_holder():
    msg = None
    global conn
    try:
       
        conn = sqlite3.connect(get_database())
        with conn:
            cur = conn.cursor()
            global sql_create_holder
            cur.execute(sql_create_holder)
            conn.commit()
            row = cur.fetchone()
            if row == None:
                msg = "Table exists holder"
            else:
                msg = "Table created holder"
            logger.info(msg)
    except sqlite3.OperationalError as e:
        msg = str(e)
    return msg

def init_user():
    msg = None
    global conn
    try:
       
        conn = sqlite3.connect(get_database())
        with conn:
            cur = conn.cursor()
            global sql_create_users
            cur.execute(sql_create_users)
            conn.commit()
            row = cur.fetchone()
            if row == None:
                msg = "Table exists user"
            else:
                msg = "Table created user"
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
            global sql_insert_holder
            global sql_insert_user
            # cur.execute(sql_insert_holder, (1,"Test note","topic","www.bla.com", timeNow))
            # cur.execute(sql_insert_user, ("espen","master"))
            cur.execute("delete from users where id > 1")
            conn.commit()
            msg = "added row"
    except sqlite3.OperationalError as e:
        print(e)
        conn.rollback()
    print(msg)








print(init_holder())
print(init_user())
# dummy_data()
