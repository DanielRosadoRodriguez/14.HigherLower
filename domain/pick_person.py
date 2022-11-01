from data import game_data
import random
this_game_data = game_data.data


def pick_person():
    """
    function that picks one person from the data file
    :return:person_picked
    """

    person_picked = random.choice(this_game_data)
    return person_picked
