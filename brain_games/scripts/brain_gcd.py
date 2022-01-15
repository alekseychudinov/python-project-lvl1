#!/usr/bin/env python


import random

import prompt

import math


def main():
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print("Hello, {0}!".format(name))
    print('What is the result of the expression?')
    count = 0
    while count < 3:
        number1 = random.randint(1, 100)
        number2 = random.randint(1, 100)
        result = math.gcd(number1, number2)
        print("Question: {0} {1}".format(str(number1), str(number2)))
        user_answer = prompt.string("Your answer: ")
        if user_answer == str(result):
            print('Correct!')
            count += 1
        else:
            print(
                "'{0}' is wrong answer ;(. Correct answer was '{1}'.\nLet's try again, {2}!".format(  # noqa
                    user_answer, result, name
                )
            )
            return
    print("Congratulations, {0}!".format(name))


if __name__ == "__main__":
    main()
