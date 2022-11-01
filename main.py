from domain import print_wellcome as pw, pick_person

pw.print_wellcome()
person1 = pick_person.pick_person()
print(f"Option A: {person1.get('name')}, {person1.get('description')} from {person1.get('country')}")
person2 = pick_person.pick_person()
print(f"Option B: {person2.get('name')}, {person2.get('description')} from {person2.get('country')}")
