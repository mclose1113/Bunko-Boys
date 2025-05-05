def evaluate_bunko_roll(round_number, roll):
    """totals the score of a persons dice(3 random int) roll in a round of Bunko


    Args:
        round_number (int): The current round number 1-6
        roll (tuple of int): a tuple containing three integers that is the 
        players dice roll
        
    Returns:
        None
    
    Side Effects:
        prints the score change resulting from the roll
        Prints "BUNKO!" if the roll triggers a BUNKO
    """
    score = 0
    bunko = False
    # setting the score to 0 right now, might change how that works later
    if roll[0] == roll[1] == roll[2]:
        if roll[0] == round_number:
            # checking for bunko 
            print("BUNKO!")
            return "BUNKO!"
        else:
            score += roll[0]
    if set(roll) == {2,4,6} and round_number % 2 == 1:
        # this checks if the round number is odd, and if it is and they have all
        # 3 different even numbers in any order(via the set) they lose points
        score -= 2
    if set(roll) == {1,3,5} and round_number % 2 == 0:
        # same thing but for odds this time
        score -= 2
    if round_number in roll:
        # this is the normal point method, sees how many die match the round num
        # and adds how many matches to the score
        score += roll.count(round_number)
    # if none of the four rules are proc'd than nothing happens with the score 
    print(f"Score: {score}")
    return score
# tests:
# print("test 1: bunko")
# evaluate_bunko_roll(1, (1, 1, 1))

# print("test 2: 3 of a kind, but not bunko")
# evaluate_bunko_roll(3, (5, 5, 5))

# print("test 3: losing combo on an odd round")
# evaluate_bunko_roll(3, (2, 4, 6))

# print("test 4: losing combo on an even round")
# evaluate_bunko_roll(2, (1, 3, 5))

# print("test 5: 2 matching rolls")
# evaluate_bunko_roll(2, (2, 3, 2))

# print("test 6: no matches")
# evaluate_bunko_roll(4, (1, 5, 6))