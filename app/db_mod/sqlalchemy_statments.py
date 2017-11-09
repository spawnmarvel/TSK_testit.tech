
from app.db_mod import sqlalchemy_declarative
import sqlite3
import datetime

conn = None
sql_select_all = "select * from holder"
sql_select_max_id = "select max(id) from holder"
sql_insert = "insert into holder (id, note, topic, published) values (?, ?, ?, ?)"


def get_all():
    msg = ""
    global conn
    try:
        conn = conn = sqlite3.connect("app/db_mod/database.db")
        with conn:
            cur = conn.cursor()
            global sql_select_all
            cur.execute(sql_select_all)
            row = cur.fetchall()
            msg = row
    except sqlite3.OperationalError as e:
        msg = str(e)
        conn.rollback()
    return msg

def get_max_id():
    msg = ""
    global conn
    try:
        conn = conn = sqlite3.connect("app/db_mod/database.db")
        with conn:
            cur = conn.cursor()
            global sql_select_all
            cur.execute(sql_select_max_id)
            row = cur.fetchall()
            msg = row
    except sqlite3.OperationalError as e:
        msg = str(e)
        conn.rollback()
    return msg


def insert(id, note, topic):
    msg = None
    global conn
    try:
        conn = conn = sqlite3.connect("app/db_mod/database.db")
        with conn:
            cur = conn.cursor()
            time_now = datetime.datetime.now()
            global sql_insert
            cur.execute(sql_insert, (id,note,topic, time_now))
            conn.commit()
            msg = "added row"
    except sqlite3.OperationalError as e:
        msg = e
        conn.rollback()
    except sqlite3.IntegrityError as e:
        msg = e
        conn.rollback()
    
    return msg


print(get_all())