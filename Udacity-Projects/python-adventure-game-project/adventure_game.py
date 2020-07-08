# an old-fashioned text-based adventure game.


import time
import random


def print_pause(string):
    print(string)
    time.sleep(2)


def intro(name, items):
    print_pause('You find yourself standing in an open field, '
                'filled with grass and yellow wildflowers.')
    print_pause('Rumor has it that a ' + name +
                ' is somewhere around here, '
                'and has been terrifying the nearby village.')
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand you hold your trusty, "
                "(but not very effective) dagger.")
    menu(name, items)


def menu(name, items):
    print_pause(" ")
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")
    print("What would you like to do?")
    validate_input(name, items)


def validate_input(name, items):
    print("(Please enter 1 or 2).")
    response = input()
    if response == '1':
        house(name, items)
    elif response == '2':
        cave(name, items)
    else:
        validate_input(name, items)


# Things that happen to the player in the house
def house(name, items):
    print_pause("You approach the door of the house.")
    print_pause("You are about to knock"
                " when the door opens and out steps a " + name)
    print_pause("Eep! This is the " + name + "'s house!")
    print_pause("The " + name + " attacks you!")
    if "Dagger" not in items:
        print_pause("You feel a bit unprepared for this,"
                    " what with only having a tiny dagger.")
    print_pause("Would you like to (1) fight or (2) run away?")
    response_house = input()
    if response_house == '1':
        fight(name, items)
    elif response_house == '2':
        run_away(name, items)
    else:
        play_again()


# Things that happen to the player goes in the cave
def cave(name, items):
    print_pause("You peer cautiously into the cave.")
    if "Dagger" in items:
        print_pause("You've been here before, "
                    "and gotten all the good stuff. "
                    "It's just an empty cave now.")
    else:
        items.append("Dagger")
        print_pause("It turns out to be only a very small cave.")
        print_pause("Your eye catches a glint of metal behind a rock.")
        print_pause("You have found the Magical Sword of Ogoroth!")
        print_pause("You discard your silly old dagger "
                    "and take the sword with you.")
    print_pause("You walk back out to the field.")
    menu(name, items)


# Things that happen when the player fights
def fight(name, items):
    if "Dagger" in items:
        win(name)
    else:
        lost(name)
    play_again()


# Things that happen when the player runs back to the field
def run_away(name, items):
    print_pause("You run back into the field."
                " Luckily, you don't seem to have been followed.")
    menu(name, items)


def win(name):
    print_pause("As the " + name + " moves to attack,"
                                   " you unsheath your new sword.")
    print_pause("The sword of Oogorth shines brightly in your hand" ""
                "as you brace yourself for the attack.")
    print_pause("But the " + name + " takes one"
                " look at your shiny new toy and runs away!")
    print_pause("You have rid the town of the " + name +
                ".You are victorious!")


def lost(name):
    print_pause("You do your best...")
    print_pause("but your dagger is no match for the " + name)
    print_pause("You have been defeated!")


def play_again():
    print_pause("Would you like to play again? (y/n)")
    play = input()
    if play == 'y':
        print("Excellent! Restarting the game...")
        # start with beginning with original settings all over again
        play_game()
    elif play == 'n':
        print_pause("Thanks for playing! See you next time.")
    else:
        play_again()


def play_game():
    items = []
    arr = ['wicked fairie', 'gorgon', 'troll', 'dragon', 'pirate']
    enemy = random.choice(arr)
    intro(enemy, items)


play_game()

# pycodestyle adventure_game.py
# to check using the pycodestyle tool for any issues and correcting
