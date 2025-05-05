def total_bunko_scores(scores_dict, filename= "bunko_scores.txt"):
    """
    Writes in a file each of the scores for each round and for each team. It then displays the total of each team's score.
    """
    
    with open(filename, 'w') as file:
        for team_name, scores in scores_dict.items():
            total = sum(scores)
            file.write(f"Team Name: {team_name}\n")
            round = 1
            for value in scores:
                file.write(f"Round {round} = {value}\n")
                round += 1
            file.write(f"{team_name}'s total score is {total}\n")