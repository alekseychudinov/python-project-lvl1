#!/usr/bin/env python


import random

import prompt


def main():
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print("Hello, {0}!".format(name))
    print('Answer "yes" if the number is even, otherwise answer "no".')
    count = 0
    while count < 3:
        number = random.randint(1, 100)
        print("Question: " + str(number))
        user_answer = prompt.string("Your answer: ")
        if (number % 2 == 0 and user_answer == "yes") or (
            number % 2 == 1 and user_answer == "no"
        ):
            print("Correct!")
            count += 1
        elif number % 2 == 0 and user_answer == "no":
            print(
                "'no' is wrong answer ;(. Correct answer was 'yes'.\nLet's try again, "  # noqa
                + name  # noqa
            )
            return
        elif number % 2 == 1 and user_answer == "yes":
            print(
                "'yes' is wrong answer ;(. Correct answer was 'no'.\nLet's try again, "  # noqa
                + name  # noqa
            )
            return
        else:
            print(
                "'"
                + user_answer  # noqa
                + "' is wrong answer ;(.\nLet's try again, "  # noqa
                + name  # noqa
            )
            return
    print("Congratulations, {0}!".format(name))


if __name__ == "__main__":
    main()
