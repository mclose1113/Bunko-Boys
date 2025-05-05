from random import randint
from evaluate_bunko_roll import evaluate_bunko_roll
from bunko_match_up import match_up
from bunko import total_bunko_scores

def bunko_game():
    """Iterates through the six rounds of the game and adds up each players
    score and determine who wins each round
    
    Side Effects:
        prints the results of each round and the total score of each player
        for each round 
    
    """
    gamestate = True
    match_up()  
    # ^ set up the match before starting the game
    total_scores = [0, 0, 0, 0]
    # added a new variable that holds all the scores
    #loop that iterates through the six rounds 
    while gamestate:
        round_num = 1
        #Each round of the game
        while round_num <= 6:
            player1_score = 0
            player2_score = 0
            player3_score = 0
            player4_score = 0
            #Continues to roll new three die for each player while no one has
            #Gotten over the 21 score to win the round
            while (player1_score <=20 and player2_score <=20 and
                player3_score <=20 and player4_score <=20):
                #Determines the players score and rolls their dice
                player1 = (dice_roll(1,6),dice_roll(1,6),dice_roll(1,6))
                #If the player rolls bunko print it and continue the loop 
                #Calls Matthew score function that requires a tuple of dice
                #numbers and the round number
                result = evaluate_bunko_roll(round_num, player1)
                if result == "BUNKO!":
                    print("BUNKO!")
                    continue
                #If the roll is not bunko then add the score for those rolls
                #to their total score 
                else:
                    player1_score += result
                #Player 2 turn
                player2 = (dice_roll(1,6),dice_roll(1,6),dice_roll(1,6))
                result = evaluate_bunko_roll(round_num, player2)
                if result == "BUNKO!":
                    print("BUNKO!")
                    continue
                else:
                    player2_score += result
                #Player 3 turn
                player3 = (dice_roll(1,6),dice_roll(1,6),dice_roll(1,6))
                result = evaluate_bunko_roll(round_num, player3)
                if result == "BUNKO!":
                    print("BUNKO!")
                    continue
                else:
                    player3_score += result
                #Player 4 turn
                player4 = (dice_roll(1,6),dice_roll(1,6),dice_roll(1,6))
                result = evaluate_bunko_roll(round_num, player4)
                if result == "BUNKO!":
                    print("BUNKO!")
                    continue
                else:
                    player4_score += result
            #Print the results after the round it done to show each players
            #score        
            print(f"Round {round_num} results:")
            print(f"Player 1 score: {player1_score}")
            print(f"Player 2 score: {player2_score}")
            print(f"Player 3 score: {player3_score}")
            print(f"Player 4 score: {player4_score}\n")
            total_scores[0] += player1_score
            total_scores[1] += player2_score
            total_scores[2] += player3_score
            total_scores[3] += player4_score
            #Add 1 to round number 
            round_num += 1
            #If the round is at the max six to end the game 
            if round_num == 6:
                gamestate = False
    total_bunko_scores(total_scores)
    
def dice_roll(min, max):
    """Returns a rolled dice based on a minimum number and max number
    
    Args:
        min(int): a minimum for the dice number
        max(int): a maximum number on the dice
        
    Returns:
        A random dice number based on the minimum and maximum
    
    """
    return randint(min, max)

if __name__ == "__main__":
    bunko_game()