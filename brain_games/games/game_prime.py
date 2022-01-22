import random

import prompt
from brain_games.is_prime import is_prime


def game_prime(name):
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
                + name
                + "!"  # noqa
            )
            return
        elif result == "no" and user_answer == "yes":
            print(
                "'yes' is wrong answer ;(. Correct answer was 'no'.\nLet's try again, "  # noqa
                + name
                + "!"  # noqa
            )
            return
        else:
            print(
                "'"
                + user_answer  # noqa
                + "' is wrong answer ;(.\nLet's try again, "  # noqa
                + name
                + "!"  # noqa
            )
            return
    print("Congratulations, {0}!".format(name))
