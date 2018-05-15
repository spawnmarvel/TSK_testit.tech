class Player():

    def __init__(self, name, onTeam, id):
        self.name = name
        self.onTeam = False
        self.id = id

    def __repr__(self):
        return self.name + " " + format(self.onTeam) + " " + format(self.id)