from app.db_mod import sqlalchemy_declarative

import sqlite3

conn = None
sql_select_all = "select * from holder"


def get_all():
    msg = ""
    global conn
    try:
        conn = conn = sqlite3.connect("database.db")
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