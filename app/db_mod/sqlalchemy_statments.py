from app.db_mod import sqlalchemy_declarative

import sqlite3
import datetime

conn = None
sql_select_all = "select * from holder order by id desc"
sql_select_max_id = "select max(id) from holder"
sql_insert = "insert into holder (id, note, topic, url, published) values (?, ?, ?, ?, ?)"
sql_delete = "Delete from holder where id = ?"


def get_all():
    msg = ""
    global conn
    try:
        conn = sqlite3.connect("app/db_mod/database.db")
        with conn:
            cur = conn.cursor()
            global sql_select_all
            cur.execute(sql_select_all)
            row = cur.fetchall()
            msg = row
    except sqlite3.OperationalError as e:
        msg = str(e)
    return msg

def get_max_id():
    msg = ""
    global conn
    try:
        conn = sqlite3.connect("app/db_mod/database.db")
        with conn:
            cur = conn.cursor()
            global sql_select_all
            cur.execute(sql_select_max_id)
            row = cur.fetchone()
            msg = row
    except sqlite3.OperationalError as e:
        msg = str(e)
    return msg


def insert(note, topic, url_to_save):
    msg = None
    global conn
    try:
        conn = conn = sqlite3.connect("app/db_mod/database.db")
        with conn:
            cur = conn.cursor()
            time_now = datetime.datetime.now()
            global sql_insert
            # get max id and increase it with 1
            tmp_id = get_max_id()
            max_id = tmp_id[0] + 1
            cur.execute(sql_insert, (max_id,note,topic,url_to_save, time_now))
            conn.commit()
            msg = "Added 1 row to sqlite3, with id " + str(max_id)
    except sqlite3.OperationalError as e:
        msg = e
        conn.rollback()
    except sqlite3.IntegrityError as e:
        msg = e
        conn.rollback()
    except sqlite3.InterfaceError as e:
        msg = e
        conn.rollback()
    
    return msg

def delete(id_):
    msg = None
    global conn
    try:
        conn = conn = sqlite3.connect("app/db_mod/database.db")
        with conn:
            cur = conn.cursor()
            global sql_delete
            cur.execute(sql_delete, (id_,))
            conn.commit()
            msg = "Delete 1 row, id " + str(id_)
    except sqlite3.OperationalError as e:
        msg = e
        conn.rollback()
    except sqlite3.IntegrityError as e:
        msg = e
        conn.rollback()
    
    return msg

sqlalchemy_declarative.init()
# print(get_all())
print(get_max_id())
x = get_max_id()
y = x[0]
print(str(y))