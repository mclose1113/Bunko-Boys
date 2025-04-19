previous_scores = {"Team A": 20,
                    "Team B": 20,
                    "Team C": 15,
                    "Team D": 40,
                    "Team E": 1,
                    "Team F": 5,
                    "Team G": 6,
                    "Team H": 30}
                    


def match_up(scores):
    """ Determines which teams from the previous round play eachother in the 
        next round based on score.

    Args:
        scores(dict): The scores of the previous teams. Does not need to be
        organized/ordered. Team names are keys and scores are values.
        
    Returns:
        new_matches(dict): The matchups of teams from the previous round
        based on scores. 
    
    Side Effects:
        prints the the new match ups from the new_matches dict.
    
    """
    
    #Sorting the scores dictionary in descending order by score.
    ordered = sorted(scores, key = lambda team: scores[team],reverse = True)
    new_matches = {}
    print( "\nThe new match-ups are: \n")
    
    #Iterating over ordered list to add to the new matches dict in pairs and
    # print a VS message.
    for team in range(0, len(ordered) - 1, 2): 
        
        new_matches[ordered[team]] = ordered[team + 1]
        print(f"{ordered[team]} VS {ordered[team + 1]}")
    
    return new_matches
     
    
match_up(previous_scores)

