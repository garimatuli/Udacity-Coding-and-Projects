# REFACTORED VERSION of elevator_advanced.py
# The goal of the program is to make your way to your new job as an engineer on the third floor.
# On the first floor, you can pick up your ID card.
# On the second floor, you can get the employee handbook, but only if you have the ID card.
# On the third floor, you can get to your job, but only if you have both the ID card and handbook.

import time


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(1)


def intro():
    print_pause("You have just arrived at your new job!")
    print_pause("You are in the elevator.")


def check_id(items):
    print_pause("You push the button for the first floor.")
    print_pause("After a few moments, you find "
                "yourself in the lobby.")
    if "ID card" in items:
        print_pause("The clerk greets you, but she has already "
                    "given you your ID card, so there is nothing "
                    "more to do here now.")
    else:
        print_pause("The clerk greets you and gives you your ID "
                    "card.")
        items.append("ID card")
    ride_elevator(items)  # Added a call here.


def check_handbook(items):
    print_pause("You push the button for the second floor.")
    print_pause("After a few moments, you find yourself "
                "in the human resources department.")
    if "handbook" in items:
        print_pause("The HR folks are busy at their desks.")
        print_pause("There doesn't seem to be much to do here.")
    else:
        print_pause("The head of HR greets you.")
        if "ID card" in items:
            print_pause("He looks at your ID card and then gives you a copy of the employee handbook.")
            items.append("handbook")
        else:
            print_pause("He has something for you, but says he can't give it to you until you go get your ID card.")
    ride_elevator(items)  # Added a call here.


def check_id_handbook(items):
    print_pause("You push the button for the third floor.")
    print_pause("After a few moments, you find yourself "
                "in the engineering department.")
    if "ID card" in items:
        print_pause("You use your ID card to open the door.")
        print_pause("Your program manager greets you and tells you that you need to have a copy of the "
                    "employee handbook in order to start work.")
        if "handbook" in items:
            print_pause("Fortunately, you got that from HR!"
                        "Congratulations! You are ready to start your new job as vice president of engineering!")
        else:
            print_pause("They scowl when they see that you don't have it, and send you back to the elevator.")
            ride_elevator(items)  # Added a call here.
    else:
        print_pause("Unfortunately, the door is locked and you can't get in."
                    "It looks like you need some kind of key card to open the door."
                    "You head back to the elevator.")
        ride_elevator(items)  # Added a call here.


def ride_elevator(items):
    print_pause("Please enter the number for the "
                "floor you would like to visit:")
    floor = input("1. Lobby\n"
                  "2. Human resources\n"
                  "3. Engineering department\n")
    if floor == '1':
        check_id(items)
    elif floor == '2':
        check_handbook(items)
    elif floor == '3':
        check_id_handbook(items)
    else:
        print_pause("Where would you like to go next?")


def play_game():
    items = []
    intro()
    ride_elevator(items)


play_game()
