import random

random_number = random.randint(1, 1)
tries = 0


def pick():
    global tries
    pick_number = int(input("pick a number from 1 to 20"))
    if pick_number > 20 or pick_number < 1:
        print("Guess from 1 - 20")
        tries += 1
        pick()
    elif pick_number != random_number:
        print("You guessed it wrong, try again")
        tries += 1
        pick()
    elif pick_number == random_number:
        print("You guessed it right!")
        print(f"you guessed {tries} times")
        retry()


def retry():
    try_again = int(input("would you like to try again? 1 for yes, any other number for no"))
    if try_again == 1:
        pick()
    if try_again != 1:
        print("good game")


pick()
