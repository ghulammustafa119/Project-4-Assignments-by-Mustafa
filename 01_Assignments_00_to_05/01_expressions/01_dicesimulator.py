
# Simulate filling two dice, three times. Prints the results of each die roll. This program is used to show how variable scope works.

# Program: Dice Simulator
# ------------------------
# Simulate rolling two dice, three times. 
# Prints the results of each die roll. This program is used
# to show how variable scope works.

# Import the random library which lets us simulate random things like dice!





import random

# Number of sides on each die to roll
NUM_SIDES = 6

def roll_dice():
    """
    Simulates rolling two dice and prints their total
    """
    die1: int = random.randint(1, NUM_SIDES)  # Randomly roll the first die
    die2: int = random.randint(1, NUM_SIDES)  # Randomly roll the second die
    total: int = die1 + die2  # Calculate the total of the two dice
    print(f"Total of two dice: {total}")  # Print the total

def main():
    die1: int = 10  # Initialize die1 in main() to 10
    print(f"die1 in main() starts as: {die1}")  # Print the initial value of die1
    roll_dice()  # Roll the dice (first time)
    roll_dice()  # Roll the dice (second time)
    roll_dice()  # Roll the dice (third time)
    print(f"die1 in main() is: {die1}")  # Print the value of die1 again after the rolls

# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()