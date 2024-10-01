import pyfiglet

title = pyfiglet.figlet_format("\nPIG (Dice Game)", font="slant")
print(title)

import random

def roll_dice():
    minimum_value = 1
    maximum_value = 6
    rolling_dice = random.randint(minimum_value, maximum_value)

    return rolling_dice

while True:
    players = input("\nEnter the number of players (2-4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
             break
        else: 
            print("Invalid input, must be between 2-4 players.")
            print("Please try again.")
    else:
        print("Invalid input, must be a digit.")
        print("Please try again.")

maximum_score = 100
player_scores = [0 for every_single_player in range(players)]  

while max(player_scores) < maximum_score:
    for player_index in range(players):
        print(f"\nPlayer {player_index + 1}, your turn has just started.")
        print(f"Total score: {player_scores[player_index]} point/s\n")
        current_score = 0

        while True:
            print("Would you like to roll? (Press 'R' if you would like to roll. Otherwise, press any 'Key' to pass.)")
            would_roll = input()
            if would_roll.upper() != "R":
                break

            rolled_value = roll_dice()
            if rolled_value == 1:
                print("You rolled a 1, turn done.")
                current_score = 0
                break
      
            else:
                current_score += rolled_value
                print(f"You rolled a {rolled_value}.")

            print(f"Current score: {current_score} point/s")    

        player_scores[player_index] += current_score
        print(f"Total score: {player_scores[player_index]} point/s")

maximum_score = max(player_scores)        
winning_player_index = player_scores.index(maximum_score)
print(f"\nPlayer {winning_player_index + 1} is the 🏆WINNER🏆 with a total score of: {maximum_score} points")        
