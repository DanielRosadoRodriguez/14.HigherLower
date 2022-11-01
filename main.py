from domain import game_core
from domain import print_wellcome as pw

pw.print_wellcome()

should_continue = True
while should_continue:
    game_core.game_core()
    user_wants_to_continue = input("Play again? y/n\n").lower()
    if user_wants_to_continue == 'n':
        should_continue = False
