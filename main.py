import random


def start_game():
    intro()
    answer = get_random_number()
    attempts = 0
    while True:  # Keep in loop till correct.
        attempts += 1  # Keep track of attempts.
        player_guess = get_guess()

        if player_guess == answer:  # player wins.
            print("You got it.")
            print(f'It took you {attempts} tries to get the answer.')
            break

        elif player_guess < answer:  # Player guessed too low.
            print("Guess higher.")

        elif player_guess > answer:  # Player guessed too high.
            print("Guess lower.")

    game_over()
    return


def intro():
    print("Hello, welcome to my guessing game.")
    return


def game_over():
    print("Goodjob and Goodbye.")


def get_random_number():
    ran_num = random.randint(1, 100)
    # print(ran_num)
    return ran_num


def get_guess():
    while True:  # Keep in loop till the proper response is given.
        try:  # Catching exceptions from float or string.

            guess = input("Please guess a number between 1 and 100.")
            guess_int = int(guess)
            if guess_int < 1:  # Check for negative numbers.
                print("Must be an integer higher than 0")
                raise ValueError
            if guess_int > 100:  # Check for numbers higher than 100.
                print("Must be an integer lower than 101")
                raise ValueError
            return guess_int
        except:
            print("invalid input.")


start_game()




