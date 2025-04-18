def total_bunko_scores(scores, filename, team_name):
    """
    Writes in a file each of the scores for each round and for each team. It then displays the total of each team's score.
    """
    total = sum(scores)
    
    with open(filename, 'w') as file:
        file.write(f"Team Name: {team_name}")
        round = 1
        for value in scores:
            file.write(f"Round {round} = {value}\n")
            round += 1
        file.write(f"{team_name}'s total score is {total}\n")