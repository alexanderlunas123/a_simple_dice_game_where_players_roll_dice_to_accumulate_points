import random

def roll_dice():
    minimum_value = 1
    maximum_value = 6
    rolling_dice = random.randint(minimum_value, maximum_value)

    return rolling_dice