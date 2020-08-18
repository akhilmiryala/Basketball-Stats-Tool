import app 
import constants

def main():
    print("\nBASKETBALL TEAM STATS TOOL")

    dashes = '----'

    print('{} MENU {}\n'.format(dashes,dashes))

    print('Here are your choices:')
    print('1) Display Team Stats')
    print('2) Quit')

    while True:
        try:
            stats_choice = input('Enter an option >= 1\n')
            stats_choice = int(stats_choice)
            if stats_choice == 2:
                return
        except NameError:
            print('Variable not found. Please enter either 1 or 2')
        except TypeError:
            print('Incorrect Type inputted. Please enter either 1 or 2')
        except ValueError:
            print("Sorry, that is not an appropriate value")
        else:
            # if stats_choice != '1':   (getting a syntax error on the first line of the if statement whenever I add this if statement to my code)
            #     print('Selection must be either 1 or 2')
            #     continue
            print('\n1) Panthers')
            print('2) Bandits')
            print('3) Warriors')
            break
          
    while True:
        try:
            team_choice = input('Enter an option >= 1\n')
            team_choice = int(team_choice)
        except NameError:
            print('Variable not found. Please enter an integer between 1 to 3')
        except TypeError:
            print('Incorrect type inputted. Please enter an integer between 1 to 3')
        except ValueError:
            print("Sorry, that is not an appropriate value")
        else:
            if team_choice < 1 or team_choice > 3:
                print('selection must be between 1 to 3')
            else:
                app.clean_data()
                app.balance_teams()
                
                if team_choice == 1:
                    print('team: {} Stats'.format(constants.TEAMS[0]))
                    print('-------------')
                    print('Total players: {}\n'.format(app.num_players_teams))
                    print('Players on team:\n')
                elif team_choice == 2:
                    print('team: {} Stats'.format(constants.TEAMS[0]))
                    print('-------------')
                    print('Total players: {}\n'.format(app.num_players_teams))
                    print('Players on team:\n')
                elif team_choice == 3:
                    print('team: {} Stats'.format(constants.TEAMS[0]))
                    print('-------------')
                    print('Total players: {}\n'.format(app.num_players_teams))
                    print('Players on team:\n')
                    
                list_of_players = app.TEAMS_COPY[team_choice - 1]
                for index in range(len(list_of_players)):
                    print(list_of_players[index]['name']+","),

                repeat = input('Would you like to continue? (y/n) (must added single or double quotes around your answer) ')
                if repeat == 'N'.lower() or repeat == 'n':
                    break
                else: 
                    continue

if __name__ == '__main__':
    main()
