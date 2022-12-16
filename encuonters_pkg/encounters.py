'''
The Search for Candor
By Adam Muenz
Last Updated: 12/16/2022
'''

# TODO: Read descriptions from a json file and send them to the encounter
# TODO: Encounters x9 (needs to be a list (or similar) and must be removed once selected)

class Encounter:
    '''
    A class to represent a possible encounter

    Attributes:
    success (str): inputed string that will give the player a success
    failure (str): inputed string that will give the player a failure
    description (str): description of what is hapening that the player will base their choice off of
    '''
    def __init__(self, success: str, failure: str, description: str):
        self.success = success
        self.failure = failure
        self.description = description

        # function to test if given response is a success or failure: takes in input. returns boolean
