'''
The Search for Candor
By Adam Muenz
Last Updated: 12/16/2022
'''

from random import choice
import sys
from encounters_pkg.encounters import next_encounter

# Upcoming features
# NOTE: Track of your losses (ie sprained ankel, broken arm) then at the end: you lost because of...
# NOTE: First choice. (Basicly play game) 2 options. forward and certain death.
# NOTE: Easy, Medium, and Hard Modes
# NOTE: Track player name and their W/L Ratio
# TODO: Write report on project


def play_game():
    '''
    Core game functionality
    '''
    successes = failures = 0
    # if I have time add an option here as the start of the game
        # probably before play_game()
    while True:
        encounter = next_encounter()
        print(encounter.description)
        # randomize if the correct choice is option 1 or 2
            # currently incorrectly typed responses count as failures
        if choice((True, False)):
            player_choice = input(f'                    Would you like to 1. {encounter.success} or 2. {encounter.failure}: ')
            if encounter.check_success(player_choice) or player_choice == "1":
                print("|"+"-"*111+"|")
                print(encounter.success_str)
                print("|"+"-"*111+"|")
                successes += 1
            else:
                print("|"+"-"*111+"|")
                print(encounter.failure_str)
                print("|"+"-"*111+"|")
                failures += 1
        else:
            player_choice = input(f'                    Would you like to 1. {encounter.failure} or 2. {encounter.success}: ')
            if encounter.check_success(player_choice) or player_choice == "2":
                print("|"+"-"*111+"|")
                print(encounter.success_str)
                print("|"+"-"*111+"|")
                successes += 1
            else:
                print("|"+"-"*111+"|")
                print(encounter.failure_str)
                print("|"+"-"*111+"|")
                failures += 1
        # check if player has won or lost the game
        if successes == 6:
            print("|<><><><><><>| Congradulations!  After a long and arguous journey you have found your way to Candor! |<><><><><>|")
            print("|"+"-"*111+"|\n\n")
            if input("Would you like to get lost again? Y/N: ").lower() == "y":
                play_game()
            else:
                print("Enjoy your time in the city.")
                sys.exit()
        elif failures == 3:
            print("|><><><><><><><><>|  Oh no! The challenges of the journey were too much for you. You are dead.  |<><><><><><><><|")
            print("|"+"-"*111+"|\n\n")
            if input("Have you considered resurrection? Y/N: ").lower() == "y":
                play_game()
            else:
                print("Thats ok. If everyone were a winner it wouldn\'t be so special.")
                sys.exit()
        print(f'|                                       You have {successes} successes and {failures} failures.                                    |')
        print("_"*113)

print("_"*113)
print("""|><><><><><><><><><><><><><><><><><><>|  Welcome to The Search for Candor |<><><><><><><><><><><><><><><><><><><|
|---------------------------------------------------------------------------------------------------------------|
|    You are an adventurer who is lost. Your goal is to find Candor; The greatest city on this or any world.    |
| Unfortunatly for you this is a dangerous part of the world. Many obsticals will come between you and your     |
|       goal. Will you be able to overcome them? Or will you succumb to the dangers that befall you?            |
|                               P.S. You need to succeed 6 times befor you fail 3 times!                        |
|---------------------------------------------------------------------------------------------------------------|""")


play_game()
