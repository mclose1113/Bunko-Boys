def total_bunko_scores(scores_dict, filename= "bunko_scores.txt"):
    """
    Writes in a file each of the scores for each round and for each team. It then displays the total of each team's score.
    
    Primary Author: 
        Connor Nguyen
    Technique(s):
        with statement

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
    
    with open(filename, 'w') as file:
        for team_name, scores in scores_dict.items():
            total = sum(scores)
            file.write(f"Player Name: {team_name}\n")
            round = 1
            for value in scores:
                file.write(f"Round {round} = {value}\n")
                round += 1
            file.write(f"{team_name}'s total score is {total}\n")