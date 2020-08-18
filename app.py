import constants
import copy 
import random

PLAYERS_COPY = copy.deepcopy(constants.PLAYERS)
TEAMS_COPY = copy.deepcopy(constants.TEAMS)
num_players_teams = len(constants.PLAYERS)/len(constants.TEAMS)

def clean_data():
    for index in range(len(PLAYERS_COPY)):
        PLAYERS_COPY[index]['height'] = PLAYERS_COPY[index]['height'].split(" ")
        PLAYERS_COPY[index]['height'] = PLAYERS_COPY[index]['height'][:1]
        PLAYERS_COPY[index]['height'][0] = int(PLAYERS_COPY[index]['height'][0])
        height = PLAYERS_COPY[index]['height'][0]
        PLAYERS_COPY[index]['height'] = height

        
        if PLAYERS_COPY[index]['experience'] == 'YES':
            PLAYERS_COPY[index]['experience'] = True
        else:
            PLAYERS_COPY[index]['experience'] = False


def balance_teams():
    index = 0
    num = 0
    for team in TEAMS_COPY:
        team = []
        while (index < num_players_teams):
            if len(PLAYERS_COPY) != 0:
                player_name = PLAYERS_COPY.pop(random.randrange(len(PLAYERS_COPY)))
                team.append(player_name)
                index += 1
        TEAMS_COPY[num] = team
        num += 1
        index = 0

# print(PLAYERS_COPY)
# print(TEAMS_COPY)
if __name__ == "__main__":
    clean_data()
    balance_teams()