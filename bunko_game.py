from argparse import ArgumentParser
from random import randint
from evaluate_bunko_roll import evaluate_bunko_roll
from bunko_match_up import match_up
from bunko import total_bunko_scores
from Players_teams import PlayerTeams
from bunko_scoreboard import bunko_score


def bunko_game(player_names=None, shuffle_teams=False):
    """Iterates through the six rounds of the game and adds up each players
    score and determine who wins each round
    
    Side Effects:
        prints the results of each round and the total score of each player
        for each round 
    
    """
    gamestate = True
    # default number of players is 4 for now 
    num_players = 4
    # init's the class with num_players
    team_splitter = PlayerTeams(num_players)
    
    if player_names:
        team_splitter.player_names = player_names
    
    else:
        # ask for their names if not Command line args
        team_splitter.ask_name()
        
    player1_name = team_splitter.player_names[0]
    player2_name = team_splitter.player_names[1]
    player3_name = team_splitter.player_names[2]
    player4_name = team_splitter.player_names[3]
        
    if shuffle_teams is not True or False:
        # ask the user if they want to shuffle the teams if not Command line arg
        shuffle_input = input("shuffle the teams? y/n:").strip().lower()
        shuffle_teams = shuffle_input == "y"
        
    # make the teams
    team_splitter.make_teams(shuffle = shuffle_teams)
    team1 = team_splitter.teams[0]
    team2 = team_splitter.teams[1]
    # print who is on a team together (havent added in the team names yet)
    print(team_splitter)
    # dict of the total scores, each key has a value of a list, the list is the 
    # round by round score, (change)it can now take the names from team_splitter
    total_scores = {name: [] for name in team_splitter.player_names}
    
    #loop that iterates through the six rounds 
    while gamestate:
        round_num = 1
        #Each round of the game
        while round_num <= 6:
            #Continues to roll new three die for each player while no one has
            #Gotten over the 21 score to win the round
            # create the score variables 
            player1_score = 0
            player2_score = 0
            player3_score = 0
            player4_score = 0
            team1_score = 0
            team2_score = 0
            bunko = False
            while team1_score < 21 and team2_score < 21:
                # changed it so that it takes the teams score, not player 
                #Determines the players score and rolls their dice
                #If the player rolls bunko print it and continue the loop 
                #Calls Matthew score function that requires a tuple of dice
                #numbers and the round number
                player1 = take_turn(round_num, player1_name)
                if player1 == "BUNKO!":
                    print("BUNKO!")
                    player1_score += 21
                    bunko = True
                    # adds the 21 to the team as well as the player 
                    if player1_name in team1:
                        team1_score += 21
                    else:
                        team2_score += 21
                    print(f"{player1_name} current score is {player1_score}")
                    if player1_name in team1:
                        print(f"team 1 score: {team1_score}")
                    else:
                        print(f"team 2 score: {team2_score}")
                    print()
                    break
                #If the roll is not bunko then add the score for those rolls
                #to their total score 
                else:
                    player1_score += player1
                    if player1_name in team1:
                        team1_score += player1
                    else:
                        team2_score += player1
                    print(f"{player1_name} current score is {player1_score}")
                    if player1_name in team1:
                        print(f"team 1 score: {team1_score}")
                    else:
                        print(f"team 2 score: {team2_score}")
                    print()
                #Player 2 turn
                player2 = take_turn(round_num, player2_name)
                if player2 == "BUNKO!":
                    print("BUNKO!")
                    player2_score += 21
                    bunko = True
                    if player2_name in team1:
                        team1_score += 21
                    else:
                        team2_score += 21
                    print(f"{player2_name} current score is {player2_score}")
                    if player2_name in team1:
                        print(f"team 1 score: {team1_score}")
                    else:
                        print(f"team 2 score: {team2_score}")
                    print()
                    break
                else:
                    player2_score += player2
                    if player2_name in team1:
                        team1_score += player2
                    else:
                        team2_score += player2
                    print(f"{player2_name} current score is {player2_score}")
                    if player2_name in team1:
                        print(f"team 1 score: {team1_score}")
                    else:
                        print(f"team 2 score: {team2_score}")
                    print()
                #Player 3 turn
                player3 = take_turn(round_num, player3_name)
                if player3 == "BUNKO!":
                    print("BUNKO!")
                    player3_score += 21
                    bunko = True
                    if player3_name in team1:
                        team1_score += 21
                    else:
                        team2_score += 21
                    print(f"{player3_name} current score is {player3_score}")
                    if player3_name in team1:
                        print(f"team 1 score: {team1_score}")
                    else:
                        print(f"team 2 score: {team2_score}")
                    print()
                    break
                else:
                    player3_score += player3
                    if player3_name in team1:
                        team1_score += player3
                    else:
                        team2_score += player3
                    print(f"{player3_name} current score is {player3_score}")
                    if player3_name in team1:
                        print(f"team 1 score: {team1_score}")
                    else:
                        print(f"team 2 score: {team2_score}")
                    print()
                #Player 4 turn
                player4 = take_turn(round_num, player4_name)
                if player4 == "BUNKO!":
                    print("BUNKO!")
                    player4_score += 21
                    bunko = True
                    if player4_name in team1:
                        team1_score += 21
                    else:
                        team2_score += 21
                    print(f"{player4_name} current score is {player4_score}")
                    if player4_name in team1:
                        print(f"team 1 score: {team1_score}")
                    else:
                        print(f"team 2 score: {team2_score}")
                    print()
                    break
                else:
                    player4_score += player4
                    if player4_name in team1:
                        team1_score += player4
                    else:
                        team2_score += player4
                    print(f"{player4_name} current score is {player4_score}")
                    if player4_name in team1:
                        print(f"team 1 score: {team1_score}")
                    else:
                        print(f"team 2 score: {team2_score}")
                    print()
            
            #Print the results after the round it done to show each players
            #score        
            print(f"Round {round_num} results:")
            # needed to change logic so now it prints their name, and then score
            print(f"{player1_name} score: {player1_score}")
            print(f"{player2_name} score: {player2_score}")
            print(f"{player3_name} score: {player3_score}")
            print(f"{player4_name} score: {player4_score}\n")
            # now prints the teams score as well as personal score 
            print(f"team 1 ({team1[0]} & {team1[1]}) score: {team1_score}")
            print(f"team 2 ({team2[0]} & {team2[1]}) score: {team2_score}\n")
            # appends the round score to the list inside of the dict
            total_scores[player1_name].append(player1_score)
            total_scores[player2_name].append(player2_score)
            total_scores[player3_name].append(player3_score)
            total_scores[player4_name].append(player4_score)
            #Add 1 to round number 
            round_num += 1
            #If the round is at the max six to end the game 
            if round_num == 7:
                continue_game = input("Would you like to replay? y/n: ")
                if continue_game.lower() == 'y':
                   round_num = 1
                else:
                    gamestate = False 
                
                #Asking if they want new teams based on score
                new_teams = input("Would you like to make new score-based"
                                  "teams? y/n: \n")
                if new_teams.lower().strip() == 'y':
                    #Making a dictionary of individual player scores
                    player_scores = {player1_name:player1_score, 
                                     player2_name:player2_score, 
                                     player3_name:player3_score,
                                     player4_name:player4_score}
                    team1, team2 = match_up(player_scores)
                else:
                    continue
                    
    
    total_bunko_scores(total_scores)
    """
    Writes in a file each of the scores for each round and for each team. It 
    then displays the total of each team's score.
    
    Args:
        scores_dict (dict): A dictionary where the keys are player names (str), 
            and the values are lists of scores (int) per round.
            
        filename (str): The name of the file to write the scores to which 
            automatically is "bunko_scores.txt".

    Returns:
        None

    Side effects:
        Creates the file specified by the filename with each team's round scores 
        and total score.
    """
    bunko_score(total_scores)
    """
    Converts a dictionary of player scores into a pandas DataFrame,
        adds a final total score column, and prints the final result.

    Args:
        player_scores (dict): A dictionary where the keys are player names (str) 
        and the values are lists of integers with the scores per round.

    Returns:
        None

    Side effects:
        Prints the final DataFrame to the console.
    """

    
def dice_roll(min=1, max=6):
    """Returns a rolled dice based on a minimum number and max number
    
    Args:
        min(int): a minimum for the dice number
        max(int): a maximum number on the dice
        
    Returns:
        A random dice number based on the minimum and maximum
    
    """
    return randint(min, max)

def take_turn(round_num, player_name):
    """Take turn is used to roll the die for the player and return the score
    
        Args:
            round_num(int): the round number
            player_name(str): the players name
        
        Returns:
            score(int): is the score for that roll 
            
        Side effects:
            prints the players name and what they scored for that turn

    """
    enter = input(f"{player_name} press enter to roll die: ")
    die1 = dice_roll()
    die2 = dice_roll()
    die3 = dice_roll()
    die = (die1, die2, die3)
    print(f"{player_name} rolled {die}")
    score = evaluate_bunko_roll(round_num, die)
    return score

def parse_args():
    parser = ArgumentParser()
    parser.add_argument("--players", nargs= 4, 
                        help= "Names for 4 players")
    parser.add_argument("--shuffle",choices=["yes", "no"], 
                        help= "Shuffle? yes or no")
    args = parser.parse_args()
    shuffle_teams = args.shuffle == "yes"
    return args, shuffle_teams

if __name__ == "__main__":
    args, shuffle_teams = parse_args()
    bunko_game(player_names=args.players, shuffle_teams=shuffle_teams)
    