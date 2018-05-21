import random as ran
from app.mod_util import player as pl

import logging
logger = logging.getLogger("utility helper")


def read_file(list_input):
    teams = []
    loop = 0
    try:
        for x in list_input:
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
    # copy list tmp, shuffel it and store in dup_teams
    tmp = teams_master[:]
    ran.shuffle(tmp)
    dup_teams_master = tmp
    ran.shuffle(teams_master)

    lim = len(teams_master)

    if len(teams_master) < 2:
        result = teams_master
    else:
        for x in range(lim):
            for y in range(lim):
                logger.info(teams_master[x].name)
                if teams_master[x] == dup_teams_master[y] or teams_master[x].onTeam ==  True:
                    pass
                else:
                    #added 21.05
                    if len(teams_master[x].name) > 2  and len(dup_teams_master[y].name) > 2:
                    # check for name len > 2 , added end
                        if not dup_teams_master[y].onTeam == True:
                            dup_teams_master[y].onTeam = True
                            teams_master[x].onTeam = True
                            result.append(teams_master[x].name + " vs " + dup_teams_master[y].name )
                            break

    return result
    

