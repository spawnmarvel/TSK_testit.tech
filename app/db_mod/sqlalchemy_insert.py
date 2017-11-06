from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
# from our module
from sqlalchemy_declarative import Base, Note

engine = create_engine("sqlite:sqlalchemy_note.db")
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

# insert a new note
note_one = Note(nt="Make CRUD db", topic="SQL")
note_two = Note(nt="Make View for CRUD db", topic="HTML/PY")
session.add(note_one)
session.add(note_two)
session.commit()
