'''
The Search for Candor: Encounters
By Adam Muenz
Last Updated: 12/16/2022
'''

import random

class Encounter:
    '''
    A class to represent a possible encounter

    Attributes:
    success (str): inputed string that will give the player a success
    failure (str): inputed string that will give the player a failure
    description (str): description of what is hapening that the player will base their choice off of
    success_str (str): description of what happens when you succeed
    failure_str (str): description of what happens when you fail
    '''
    def __init__(self, success: str, failure: str, description: str, success_str: str, failure_str: str):
        self.success = success
        self.failure = failure
        self.description = description
        self.success_str = success_str
        self.failure_str = failure_str

    def check_success(self, player_choice: str) -> bool:
        '''
        Checks if the players input was correct

        Parameters:
        player_choice (str): input from player tested against self.success

        Return:
        True: if player_choice == self.success
        False: if player_choice == self.failure
        '''
        if player_choice.lower() == self.success.lower():
            return True
        if player_choice.lower() == self.failure.lower():
            return False
        print("Do you not know how to type?")

# create list
ENCOUNTERS = []

# append objects to list
# TODO: 8 of these minimum in list
ENCOUNTERS.append(Encounter(
    "Dodge forward S",
    "Dodge backward F",
    """Lorem ipsum dolor sit amet,
    consectetur adipiscing elit,
    sed do eiusmod tempor incididunt
    ut labore et dolore magna aliqua.""",
    """This is what id say to you if you got a success""",
    """And this is why you failed"""
))
ENCOUNTERS.append(Encounter(
    "Stand Still S",
    "Run Away F",
    """This is a second option to test random grab and removal of list items.""",
    "You did it bro",
    "Big oof"
))
ENCOUNTERS.append(Encounter(
    "Success",
    "Failure",
    "This is the description of 3",
    "You did it",
    "You didnt do it"
))
ENCOUNTERS.append(Encounter(
    "Success",
    "Failure",
    "This is the description of 4",
    "You did it",
    "You didnt do it"
))
ENCOUNTERS.append(Encounter(
    "Success",
    "Failure",
    "This is the description of 5",
    "You did it",
    "You didnt do it"
))
ENCOUNTERS.append(Encounter(
    "Success",
    "Failure",
    "This is the description of 6",
    "You did it",
    "You didnt do it"
))
ENCOUNTERS.append(Encounter(
    "Success",
    "Failure",
    "This is the description of 7",
    "You did it",
    "You didnt do it"
))
ENCOUNTERS.append(Encounter(
    "Success",
    "Failure",
    "This is the description of 8",
    "You did it",
    "You didnt do it"
))
ENCOUNTERS.append(Encounter(
    "Success",
    "Failure",
    "This is the description of 9",
    "You did it",
    "You didnt do it"
))
ENCOUNTERS.append(Encounter(
    "Success",
    "Failure",
    "This is the description of 10",
    "You did it",
    "You didnt do it"
))

def next_encounter() -> Encounter:
    '''
    Picks the next encounter and removes it from the encounters list

    Return:
    encounter (Encounter): Random instance of encounter from ENCOUNTERS List
    '''
    global ENCOUNTERS
    encounter = random.choice(ENCOUNTERS)
    ENCOUNTERS.remove(encounter)
    return encounter
