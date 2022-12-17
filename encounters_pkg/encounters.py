'''
The Search for Candor: Encounters
By Adam Muenz
Last Updated: 12/16/2022
'''

# TODO: Read descriptions from a json file and send them to the encounter... Maybe not. See if have time
# TODO: Encounters x8 (needs to be a list (or similar) and must be removed once selected)

class Encounter:
    '''
    A class to represent a possible encounter

    Attributes:
    success (str): inputed string that will give the player a success
    failure (str): inputed string that will give the player a failure
    description (str): description of what is hapening that the player will base their choice off of
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
        while True:
            if player_choice.lower() == self.success.lower():
                return True
            if player_choice.lower() == self.failure.lower():
                return False
            print("Please choose either 1 or 2")

# create list
encounters = []

# append objects to list
# TODO: 8 of these minimum in list
encounters.append(Encounter(
    "Dodge forward", "Dodge backward",
    """Lorem ipsum dolor sit amet,
    consectetur adipiscing elit,
    sed do eiusmod tempor incididunt
    ut labore et dolore magna aliqua.""",
    """This is what id say to you if you got a success""",
    """And this is why you failed"""
))
encounters.append(Encounter(
    "Stand Still", "Run Away",
    """This is a second option to test random grab and removal of list items.""",
    "You did it bro",
    "Big oof"
))