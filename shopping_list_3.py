import random
import os

high_score = [7]
first_place = ["Jim-Bob"]
low = 1
high = 10


def clear_screen():
    """Looks at system;
    Runs 'nt' for all modern versions of Windows;
    Runs 'clear' if on a non-Windows computer;
    """
    os.system("cls" if os.name == "nt" else "clear")


def welcome_to_game():
    """Welcomes the player to the game and tells the
    current high score and holder.
    """
    print("""
    ================================================
    Welcome to the Number Guessing Extravaganza!!!!
    ================================================
    """)

    print("""
    The rules are simple; choose a number between 1
    and 10, and we will tell you if the secret
    number is higher or lower than that. Try and
    guess the secret number in as few guesses as
    possible!
    """)
    print("""
    The current high score is {}, held by {}.
    Try and beat it!
    """.format(high_score[0], first_place[0]))
    # This is a Test Line
    # print("The number is {}".format(secret_number))


def start_game():
    """Welcomes user, picks a number between the low and high
    variables, then asks user for a guess;
    If guess is wrong, tells user if their guess was too
    low or too high;
    If guess is right, tells user they won, and if they beat
    the high score asks them for their name;
    Puts high score in high_score variable and sets
    name to first place;
    Asks user if they would like to play again.
    """
    global high_score
    global first_place
    secret_number = random.randint(low, high)
    attempts = 0
    welcome_to_game()
    while True:
        try:
            guess = int(input("What is your guess?  "))
        except ValueError:
            print("Please enter a whole number!")
            continue
        if guess == secret_number:
            attempts += 1
            print("You got it!")
            print(
              "You guessed the secret number in {} try(s)!".format(attempts))
            high_score.sort()
            if high_score[0] > attempts:
                first_place[0] = input("What is your name? ")
                high_score.insert(0, attempts)

                print("You have the new high score!")
            else:
                print("""The high score is currently {},
                      held by {}""".format(high_score[0], first_place[0]))

            print("Thanks for playing!")
            replay = input("""
                           Would you like to play again? [y]es or [n]o? """)
            if replay == "n":
                print("Thanks for playing!")
                break
            if replay == "y":
                clear_screen()
                start_game()

        if 1 <= guess < secret_number:
            attempts += 1
            print("Too low!")
            continue
        if 11 >= guess > secret_number:
            attempts += 1
            print("Too high!")
            continue
        if guess > 10:
            print("The number must be between 1 and 10.")
            continue
        if guess < 1:
            print("The number must be between 1 and 10.")
            continue

if __name__ == '__main__':
    """Starts game if being run from script,
    not imported
    """
    start_game()
