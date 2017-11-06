# http://pythoncentral.io/introductory-tutorial-python-sqlalchemy/
# 3 most important components for SQLAlchemy
# A Table that represents a table in a database.
# A mapper that maps a Python class to a table in a database.
# A class object that defines how a database record maps to a normal Python object.

import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class Note(Base):
    # note table
    __tablename__ = "note"
    id = Column(Integer, primary_key=True)
    nt = Column(String(200), nullable=False)
    topic = Column(String(20), nullable=False)
    published = Column(DateTime, default=func.now())


#class Holder(Base):
#    # holder table
#    __tablename__ = "holder"
#    id = Column(Integer, primary_key=True)
#    topic = Column(String(20))
#    #Foreign key to note
#    note_id = Column(Integer, ForeignKey("note.id"))

# Create an engine that stores data in the local directory's
engine = create_engine("sqlite:sqlalchemy_note.db")
# Create all tables in the engine. This is equivalent to "Create Table"
Base.metadata.create_all(engine)