import pandas as pd
"""
Converts a dictionary of player scores into a pandas DataFrame,
    adds a total score column, and prints the final result.

Args:
    player_scores (dict): A dictionary where the keys are player names (str) and the values are lists of 
        integers with the scores per round.

Returns:
     None

Side effects:
    Prints the final DataFrame to the console.
"""

def bunko_score(player_scores):
    df = pd.DataFrame.from_dict(player_scores)
    
    df = df.transpose() #Switches rows and columns for an easier read

    round_columns = [f"Round {i+1}" for i in range(6)]

    df.columns = round_columns
    
    df["Total Player Score"] = df.sum(axis=1) #adds a total score column and sums each row

    print(df.to_string()) 