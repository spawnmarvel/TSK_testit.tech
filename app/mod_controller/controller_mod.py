from app.mod_db import sqlalchemy_statments
from app.mod_models import notes_mod

def make_notes():
    print("controller.....->")
    tmp = sqlalchemy_statments.get_all()
    for x in range(len(tmp)):
        # print(tmp[x])
        for n in tmp[x]:
            # pass
            print("test")
            # item = notes_mod.Notes(n[0], n[1], n[2], n[3], n[4])


# make_notes()