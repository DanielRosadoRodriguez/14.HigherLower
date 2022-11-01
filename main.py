from domain import print_wellcome as pw, pick_person

pw.print_wellcome()
person1 = pick_person.pick_person()
person2 = pick_person.pick_person()


points = 0
while True:
    print(f"Option A: {person1.get('name')}, {person1.get('description')} from {person1.get('country')}")
    print(f"Option B: {person2.get('name')}, {person2.get('description')} from {person2.get('country')}")
    option = input("Insert the one you think is the highest: \n").lower()

    print(f"{person1.get('name')} has {person1.get('follower_count')}")
    print(f"{person2.get('name')} has {person2.get('follower_count')}")
    if option == "a" and person1.get('follower_count') > person2.get('follower_count'):
        print("You win!")
        person1 = person2
        person2 = pick_person.pick_person()
        points += 1
    elif option == "b" and person2.get('follower_count') > person1.get('follower_count'):
        print("You win!")
        person1 = person2
        person2 = pick_person.pick_person()
        points += 1
    else:
        print("You lose")
        print(f"You got {points}")
        break
