from app.db_mod.sqlalchemy_declarative import Note, Base
from sqlalchemy import create_engine

engine = create_engine("sqlite:sqlalchemy_note.db")
Base.metadata.bind = engine
from sqlalchemy.orm import sessionmaker

DBSession = sessionmaker()
DBSession.bind = engine
session = DBSession()

#query
def get_notes():
    li = ["start"]
    for n in session.query(Note).all():
        res = n.topic
        li.append(res)
    return li

print(get_notes())
