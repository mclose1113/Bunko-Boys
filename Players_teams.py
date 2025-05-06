import random
class PlayerTeams:
    def __init__(self, num_players):
        """Init's the class with the given number of player playing the game.

        Args:
            num_players (int): number of players in given bunko game.
        """
        self.num_players = num_players
        self.player_names = []
        self.teams = []
    def ask_name(self):
        """Asks the players for their names and then adds it to the list of name
        
        Side effects:
            self.player_names (list of str): appends the names of given players
        """
        for player in range(self.num_players):
            name = input(f"what is player {player + 1} name?:")
            self.player_names.append(name)

    def make_teams(self, shuffle = False):
        """Makes teams of 2 people per team.

        Args:
            shuffle (bool, optional): if stated as true, then it shuffles the 
            players names before making teams. Defaults to False.
        """
        names = self.player_names[:]
        if shuffle:
            random.shuffle(names)
            
        # goes up by 2 to create teams of 2
        for player in range(0, len(names), 2):
            # check if there is an uneven ammount of players
            if player + 1 < len(names):
                # teams made by taking 2 players next to eachother in the list
                player1, player2 = names[player:player + 2]
                # tuple of the players names 
                self.teams.append((player1, player2))
            # if it is uneven, it lets the last player know
            else:
                print(f"{names[player]} has no teammate")
    def __str__(self):
        # magic method to print who is in a team together
        result = ""
        for team in self.teams:
            result += f"Team: {team[0]} and {team[1]}\n"
        return result
#tests
# pt = PlayerTeams(4) #tests if it works with 4 people
# pt.player_names = ["matty", "fatty", "gyatty", "latty"] 
# pt.make_teams(shuffle=True)
# print("teams:", pt.teams)
# pt = PlayerTeams(5)  # tests if it works with 5 people
# pt.player_names = ["matty", "fatty", "gyatty", "latty", "ratty"]
# pt.make_teams(shuffle=True)
# print("teams with 5 players:", pt.teams)
# should say that someone doesnt have a teammate