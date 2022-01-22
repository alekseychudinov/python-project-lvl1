import random

import prompt


def game_even(name):
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
                + name
                + "!"  # noqa
            )
            return
        elif number % 2 == 1 and user_answer == "yes":
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
