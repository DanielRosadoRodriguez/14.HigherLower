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


def get_formatted_name(person):
    return f"{person.get('name')}, {person.get('description')} from {person.get('country')}"


def get_formatted_follower_count(person):
    return f"{person.get('name')} has {person.get('follower_count')}"


def game_core():
    """
    main function of the game
    :return: None
    """
    person1 = pick_person()
    person2 = pick_person()
    points = 0
    while True:
        print(f"Option A: {get_formatted_name(person1)}")
        print(f"Option B: {get_formatted_name(person2)}")
        option = input("Insert the one you think is the highest: \n").lower()

        print(get_formatted_follower_count(person1))
        print(get_formatted_follower_count(person2))
        if option == "a" and person1.get('follower_count') > person2.get('follower_count'):
            print("You win!")
            person1 = person2
            person2 = pick_person()
            points += 1
        elif option == "b" and person2.get('follower_count') > person1.get('follower_count'):
            print("You win!")
            person1 = person2
            person2 = pick_person()
            points += 1
        else:
            print("You lose")
            print(f"You got {points}")
            break
