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
        player_choice (str): input from player

        Return:
        True: if player_choice == self.success
        False: if player_choice == self.failure
        '''
        if player_choice.lower() == self.success.lower():
            return True
        if player_choice.lower() == self.failure.lower():
            return False

# create list
ENCOUNTERS = []

# append objects to list
ENCOUNTERS.append(Encounter(
    "Continue Forward",
    "Attack!",
    """|                    You find yourself in a small meadow. As far as you can tell it is empty.                   |
|---------------------------------------------------------------------------------------------------------------|\n""",
    "|                        After taking a moment to enjoy the calm you continue on your journey.                  |",
    """|   You swing your weapon at the open air, then again, and again! If there were music playing this could be a   |
|                 cool montage. Unfortunatly for you there is no music so you just look silly.                  |"""
))
ENCOUNTERS.append(Encounter(
    "Stand Still",
    "Run Away",
    """|    As you walk through a long gorge you feel the ground shake. Oh no! A rockalanche is coming right at you.   |
|---------------------------------------------------------------------------------------------------------------|\n""",
    "|           Somehow standing still was the right choice. What a relief. You continue on your journey.           |",
    """|              You flee from the falling boulders. Luckily you avoided the large rocks.                         |
|   Unluckily you were peppered by a plethora of pesky pebbles. You continue on your journey cut and bruised.   |"""
))
ENCOUNTERS.append(Encounter(
    "Refuse",
    "Give him all your money (about $3.50)",
    """|                                A bandit jumps you and demands all your money!                                 |
|---------------------------------------------------------------------------------------------------------------|\n""",
    """|   It was at this point you relized that the bandit was about eight stories tall and was a crustacean    |
|             from the Paleolithic Era. You continue on your way wondering why he needed $3.50                  |""",
    """| You give the bandit your money. He thanks you and then you realize that he was actualy an eight stories tall  |
|  crustacean from the Paleolithic Era. Now that he got your money you can count on him coming back for more.   |"""
))
ENCOUNTERS.append(Encounter(
    "Stop and help",
    "Continue on your way",
    """|                 You encounter an old woman attempting to place a wheel on her carriage.                       |
|---------------------------------------------------------------------------------------------------------------|\n""",
    "|               After helping her repair her carriage she cooks you a hearty meal as thanks.                    |",
    "|      The rest of the day you feel bad for not helping. You cant sleep all night due to your conscience.       |"
))
ENCOUNTERS.append(Encounter(
    "Continue on through the night",
    "Join the party",
    """|       As the sun is going down you come upon a group of merchants eating and drinking around a fire.          |
|---------------------------------------------------------------------------------------------------------------|\n""",
    "|                  With great resolve you continue on through the night making great time.                      |",
    "|         You eat and drink merily with the strangers. To bad you wake up to an incision over your kidney.      |"
))
ENCOUNTERS.append(Encounter(
    "Sidestep",
    "Run directly away from it.",
    """| You are walking through the forest when you hear a loud snap behind you. A tree is falling right towards you! |
|---------------------------------------------------------------------------------------------------------------|\n""",
    "|                                            Wow. That was easy.                                                |",
    "|       Do you think you're in an action movie? Because you're not. The tree falls and strikes your head        |"
))
ENCOUNTERS.append(Encounter(
    "Walk across",
    "Find a ford",
    """|                               You come to a river. It doesn't look too deep.                                  |
|---------------------------------------------------------------------------------------------------------------|\n""",
    "|                  The water was cool and refreshing. Luckly there wern't any river beasts                      |",
    "|                Hows a car going to help? Ha I'm only joking. You walk for a few miles and find one.           |"
))
ENCOUNTERS.append(Encounter(
    "Use your weapon",
    "Use karate",
    """|                               A group of goblins suround you ready for battle                                 |
|---------------------------------------------------------------------------------------------------------------|\n""",
    "|            You swing your weapon in an impressive display of prowess. The goblins run away in fear              |",
    """|        You attack the goblins with karate! You quickly remember that you dont know karate.                    |
|                               The goblins laugh at you until you wonder off in shame.                         |"""
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
