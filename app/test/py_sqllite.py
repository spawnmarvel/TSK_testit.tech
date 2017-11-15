# test sql lite
# http://zetcode.com/db/sqlitepythontutorial/
import sqlite3

conn = None

def init():
    try:
        global conn
        conn = sqlite3.connect("database.db")
        print("db open")
        conn.execute("if not exists create table test(id INT, name TEXT)")
        print("table created")
    except sqlite3.OperationalError:
        print("table already here")

def build():
    msg = ""
    global conn
    try:
        conn = sqlite3.connect("database.db")
        with conn:
            cur = conn.cursor()
            cur.execute("insert into test(id, name) values (?,?)", (3, "ips"))
            conn.commit()
            msg = "added rows"
    except:
        conn.rollback()
    finally:
        conn.close()
    print(msg)

def load():
    global conn
    conn = sqlite3.connect("database.db")
    with conn:
        cur = conn.cursor()
        cur.execute("select * from test")
        rows = cur.fetchall()
        for r in rows:
            print(r)


def take_away():
    global conn
    conn = sqlite3.connect("database.db")
    with conn:
        cur = conn.cursor()
        cur.execute("delete from test where id = 2")


#init()
#build()
load()
#take_away()
#load()
# https://stackoverflow.com/questions/27474306/with-pythons-sqlite3-module-can-i-save-the-in-memory-db-to-disk-after-creating