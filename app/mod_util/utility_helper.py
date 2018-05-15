import random as r
from app.mod_util import player as pl


def read_file(list_input):
    teams = []
    loop = 0
    try:
        for x in list_input:
            # print(x)
            make_player = pl.Player(x, False, loop)
            teams.append(make_player)
            loop = loop + 1
    except Exception as e:
        # print(format(e))
        pass
    return teams


def make_random(li_input):

    result = []
    teams_master = read_file(li_input)
    # print(teams_master)
    tmp = teams_master[:]
    rv = r.shuffle(tmp)
    # print("rand "+ format(tmp))
    

    dup_teams_master = tmp

    lim = len(teams_master)
    # print("Size of list " + format(len(teams_master)))
    dic_team = {}
    team = 0
    if len(teams_master) < 2:
        result = teams_master
    else:
        for x in range(lim):
            for y in range(lim):
                if teams_master[x] == dup_teams_master[y] or teams_master[x].onTeam ==  True:
                    pass
                    # we are looking at ourself and we are taken
                else:
                    if not dup_teams_master[y].onTeam == True:
                        # print("Team")
                        # print("   " + format(teams_master[x]) + " " + format(dup_teams_master[y]))
                        dup_teams_master[y].onTeam = True
                        teams_master[x].onTeam = True
                        result.append(teams_master[x].name + " vs " + dup_teams_master[y].name )
                        break
    return result
    #print("\n" + format(teams_master))

