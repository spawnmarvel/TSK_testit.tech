"""___"""
import sqlite3
import datetime
import logging
from app.mod_db import sqlalchemy_declarative



CONN = None
# DATABASE_ = sqlalchemy_declarative.get_database()
DATABASE_ = "database_.db"
#holder
SQL_SELECT_ALL = "select * from holder order by id desc"
SQL_SELECT_MAX_ID = "select max(id) from holder"
SQL_INSERT = "insert into holder (note, topic, url, published) values (?, ?, ?, ?)"
SQL_DELETE = "Delete from holder where id = ?"
#user
SQL_SELECT_USER = "select usern from users where id = 1"

LOGGER = logging.getLogger(__name__)

def get_database():
    """___"""
    global DATABASE_
    return DATABASE_

def get_all():
    """___"""
    msg = ""
    global CONN
    try:
        CONN = sqlite3.connect(get_database())
        with CONN:
            cur = CONN.cursor()
            global SQL_SELECT_ALL
            cur.execute(SQL_SELECT_ALL)
            row = cur.fetchall()
            msg = row
            LOGGER.debug(msg)
    except sqlite3.OperationalError as error_:
        msg = str(error_)
        LOGGER.debug(msg)
    return msg

def get_user():
    """___"""
    msg = ""
    global CONN
    try:
        CONN = sqlite3.connect(get_database())
        with CONN:
            cur = CONN.cursor()
            global SQL_SELECT_USER
            cur.execute(SQL_SELECT_USER)
            row = cur.fetchone()
            msg = row
            # print(msg)
            LOGGER.debug(msg)
    except sqlite3.OperationalError as error_:
        msg = str(error_)
        LOGGER.debug(msg)
    return msg

def get_max_id():
    """___"""
    msg = ""
    global CONN
    try:
        CONN = sqlite3.connect(get_database())
        with CONN:
            cur = CONN.cursor()
            global SQL_SELECT_ALL
            cur.execute(SQL_SELECT_MAX_ID)
            row = cur.fetchone()
            msg = row
    except sqlite3.OperationalError as error_:
        msg = str(error_)
    LOGGER.debug(msg)
    return msg


def insert(note, topic, url_to_save):
    """___"""
    msg = None
    global CONN
    try:
        CONN = sqlite3.connect(get_database())
        with CONN:
            cur = CONN.cursor()
            time_now = datetime.datetime.now()
            global SQL_INSERT
            # get max id and increase it with 1
            # tmp_id = get_max_id()
            # max_id = tmp_id[0] + 1
            # changed to autoincrement in sqlite
            cur.execute(SQL_INSERT, (note, topic, url_to_save, time_now))
            CONN.commit()
            max_id = get_max_id()
            msg = "Added 1 row to sqlite3, with id " + str(max_id)

    except sqlite3.OperationalError as error_:
        msg = error_
        CONN.rollback()
    except sqlite3.IntegrityError as error_:
        msg = error_
        CONN.rollback()
    except sqlite3.InterfaceError as error_:
        msg = error_
        CONN.rollback()
    LOGGER.debug(msg)
    return msg

def delete(id_):
    """___"""
    msg = None
    global CONN
    try:
        CONN = sqlite3.connect(get_database())
        with CONN:
            cur = CONN.cursor()
            global SQL_DELETE
            cur.execute(SQL_DELETE, (id_,))
            CONN.commit()
            msg = "Delete 1 row, id " + str(id_) + "."
    except sqlite3.OperationalError as error_:
        msg = error_
        CONN.rollback()
    except sqlite3.IntegrityError as error_:
        msg = error_
        CONN.rollback()
    LOGGER.debug(msg)
    return msg

sqlalchemy_declarative.init_holder()
sqlalchemy_declarative.init_user()
# sqlalchemy_declarative.dummy_data()
# print(get_all())
#print(get_max_id())
#x = get_max_id()
#y = x[0]
#print(str(y))
# print(get_user())
