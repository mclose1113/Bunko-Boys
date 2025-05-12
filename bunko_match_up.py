# Test data
# previous_scores = {"Player A": 20,
#                     "Player B": 20,
#                     "Player C": 15,
#                     "Team D": 40,}                    
                    


def match_up(scores):
    """ Determines which players will comprise the teams of a subsequent match
        based on score.
    Args:
        scores(dict): The scores of the previous teams.
        Team names are keys and scores are values.
        
    Returns:
        new_matches(dict): The matchups of players in teams
        from the previous round based on scores. 
    
    Side Effects:
        prints the the new teams from the new_matches dict.
    
    """
    
    #Sorting the scores dictionary in descending order by score.
    ordered = sorted(scores, key = lambda player: scores[player],reverse = True)
    #Assigning teams
    team1 = (ordered[0], ordered[3])
    team2 = (ordered[1],ordered[2])
    print(f"Team 1 is now {team1[0]} & {team1[1]}! \n"
          f"Team 2 is now {team2[0]} & {team2[1]} \n")
    return team1, team2
     
#Test
# match_up(previous_scores)

