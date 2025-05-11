# Documentation 
## What is Bunko?
### Rules:
Bunko is a dice game usually with a number of people divisible by 4 with teams 
of 2 people each. it is usually 4 people(2 teams) per indivisual game, and each
player takes turns rolling three dice to earn points. in each game there is a
round system, a game lasts 6 rounds, and a round ends when someone gets to 21
### Scoring
Scoring can be a little complicated at first, but easy once you get the hang of
it. During each round, players try to roll the same number on the dice as the 
current round number. for example, you want to roll a 1 if its round 1.
one point is given for each die that matches the round number. but there is 
special scoring for getting 3 of the same number on every die, if you get 3 of 
the same number that matches the round number, then you get a Bunko! and you 
get 21 points. while if you roll 3 of the same number that doesnt match the 
round number, then you are given 5 points. and finally, there is a way to lose 
points! if you roll a 2, 4, and 6, (all different even numbers) on an odd round,
then you lose 2 points! same goes for getting all differnt odd numbers on even 
rounds, ex: rolling a 1,3,5 on an even round such as round 2. 
### how to win
At the end of 6 rounds, whoever has the most rounds won is the winner! ties can 
also happen. there is also a consididation prize for the person with the most 
bunkos usually. 
## Atribution Table: 
Method/Function---------Primary author----------Techniques demonstrated

make_teams()------------Matthew Close-----------Sequence Unpacking

str() in PlayerTeams----Matthew Close-----------Magic Methods

bunko_game()---Ethan Patrick------- f-strings

dice_roll()--Ethan Patrick-------- Optional Parameters 


## sources: 
Matthew used stackoverflow in order to figure out how to itterate over a 
dictionary of lists, which was nessassary because we can now track score round 
to round, and still have it inside the same dictionary labeled by the player
https://stackoverflow.com/questions/24746712/dictionary-iterating-for-dict-vs-for-dict-items

Matthew used stackoverflow to try to help impliment sequenced unpacking into the 
make_teams() method of the PlayerTeams class 
https://stackoverflow.com/questions/33956772/extended-sequence-unpacking-in-python3 

Matthew used stackoverflow to learn how to impliment the shuffle method of 
random, and how it works with lists (also because of the make_teams() method). 
https://stackoverflow.com/questions/976882/shuffling-a-list-of-objects

Ethan watched a Youtube video that explained the game to help understand
how the loop should work and when there is a winner 
https://www.youtube.com/watch?v=qNgm0ThJZ2w

bunko rules:
https://www.dicegamedepot.com/bunco-rules/?srsltid=AfmBOoqWetMBg_sSTociGRKYCSG9V16xbmqvYttA56SAvFD_4NKIeA4t