#!/usr/bin/env python


import random

import prompt


def main():
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print("Hello, {0}!".format(name))
    print("What number is missing in the progression?")
    count = 0
    while count < 3:
        length_progression = random.randint(5, 15)
        index_of_skip_element = random.randint(0, length_progression - 1)
        step_progression = random.randint(1, 10)
        start_progression = random.randint(1, 100)
        stop_progression = (
            start_progression + step_progression * length_progression
        )
        progression = range(
            start_progression, stop_progression, step_progression
        )

        str_progression = ""
        counter = 0
        while counter < length_progression:
            if counter != index_of_skip_element:
                str_progression += str(progression[counter]) + " "
            else:
                str_progression += ".. "
            counter += 1

        print("Question: " + str_progression)
        user_answer = prompt.string("Your answer: ")
        if user_answer == str(progression[index_of_skip_element]):
            print("Correct!")
            count += 1
        else:
            print(
                "'{0}' is wrong answer ;(. Correct answer was '{1}'.\nLet's try again, {2}!".format(  # noqa
                    user_answer, progression[index_of_skip_element], name
                )
            )
            return
    print("Congratulations, {0}!".format(name))


if __name__ == "__main__":
    main()
