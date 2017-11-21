"""___"""
import sqlite3
import datetime
import logging
from app.mod_db import sqlalchemy_declarative



CONN_ = None
DATABASE_ = "app/mod_db/DATABASE.db"
SQL_SELECT_ALL = "select * from holder order by id desc"
SQL_SELECT_MAX_ID = "select max(id) from holder"
SQL_INSERT = "insert into holder (id, note, topic, url, published) values (?, ?, ?, ?, ?)"
SQL_DELETE = "Delete from holder where id = ?"

LOGGER_ = logging.getLogger(__name__)

def get_database():
    """___"""
    global DATABASE_
    return DATABASE_

def get_all():
    """___"""
    msg = ""
    global CONN_
    try:
        CONN_ = sqlite3.connect(get_database())
        with CONN_:
            cur = CONN_.cursor()
            global SQL_SELECT_ALL
            cur.execute(SQL_SELECT_ALL)
            row = cur.fetchall()
            msg = row
            LOGGER_.debug(msg)
    except sqlite3.OperationalError as error_:
        msg = str(error_)
        LOGGER_.debug(msg)
    return msg

def get_max_id():
    """___"""
    msg = ""
    global CONN_
    try:
        CONN_ = sqlite3.connect(get_database())
        with CONN_:
            cur = CONN_.cursor()
            global SQL_SELECT_ALL
            cur.execute(SQL_SELECT_MAX_ID)
            row = cur.fetchone()
            msg = row
    except sqlite3.OperationalError as error_:
        msg = str(error_)
    LOGGER_.debug(msg)
    return msg


def insert(note, topic, url_to_save):
    """___"""
    msg = None
    global CONN_
    try:
        CONN_ = sqlite3.connect(get_database())
        with CONN_:
            cur = CONN_.cursor()
            time_now = datetime.datetime.now()
            global SQL_INSERT
            # get max id and increase it with 1
            tmp_id = get_max_id()
            max_id = tmp_id[0] + 1
            cur.execute(SQL_INSERT, (max_id, note, topic, url_to_save, time_now))
            CONN_.commit()
            msg = "Added 1 row to sqlite3, with id " + str(max_id)

    except sqlite3.OperationalError as error_:
        msg = error_
        CONN_.rollback()
    except sqlite3.IntegrityError as error_:
        msg = error_
        CONN_.rollback()
    except sqlite3.InterfaceError as error_:
        msg = error_
        CONN_.rollback()
    LOGGER_.debug(msg)
    return msg

def delete(id_):
    """___"""
    msg = None
    global CONN_
    try:
        CONN_ = sqlite3.connect(get_database())
        with CONN_:
            cur = CONN_.cursor()
            global SQL_DELETE
            cur.execute(SQL_DELETE, (id_,))
            CONN_.commit()
            msg = "Delete 1 row, id " + str(id_) + "."
    except sqlite3.OperationalError as error_:
        msg = error_
        CONN_.rollback()
    except sqlite3.IntegrityError as error_:
        msg = error_
        CONN_.rollback()
    LOGGER_.debug(msg)
    return msg

sqlalchemy_declarative.init()
# print(get_all())
#print(get_max_id())
#x = get_max_id()
#y = x[0]
#print(str(y))
