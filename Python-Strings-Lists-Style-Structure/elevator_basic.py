
import time


def print_msg(str):
    print(str)
    time.sleep(2)


def intro():
    print_msg("You have just arrived at your new job!")
    print_msg("You are in the elevator.")
    validate_input()


def menu():
    print("1. Lobby")
    print("2. Human resources")
    print("3. Engineering department")


def validate_input():
    print_msg("Please enter the number for the floor you would like to visit:")
    menu()
    response = input()
    if response == '1':
        print_msg("You push the button for the first floor.")
        print_msg("After a few moments, you find yourself in the lobby.")
    elif response == '2':
        print_msg("You push the button for the second floor.")
        print_msg("After a few moments, you find yourself in the human resources department.")
    elif response == '3':
        print_msg("You push the button for the third floor.")
        print_msg("After a few moments, you find yourself in the engineering department.")
    else:
        validate_input()
    print_msg("Where would you like to go next?")
    validate_input()


intro()
