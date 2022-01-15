#!/usr/bin/env python


import random

import prompt
from brain_games.is_prime import is_prime


def main():
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print("Hello, {0}!".format(name))
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    count = 0
    while count < 3:
        number = random.randint(2, 100)
        print("Question: " + str(number))
        result = is_prime(number)
        user_answer = prompt.string("Your answer: ")
        if result == user_answer:
            print("Correct!")
            count += 1
        elif result == "yes" and user_answer == "no":
            print(
                "'no' is wrong answer ;(. Correct answer was 'yes'.\nLet's try again, "  # noqa
                + name  # noqa
            )
            return
        elif result == "no" and user_answer == "yes":
            print(
                "'yes' is wrong answer ;(. Correct answer was 'no'.\nLet's try again, "  # noqa
                + name  # noqa
            )
            return
        else:
            print(
                "'"
                + user_answer
                + "' is wrong answer ;(.\nLet's try again, "
                + name
            )
            return
    print("Congratulations, {0}!".format(name))


if __name__ == "__main__":
    main()