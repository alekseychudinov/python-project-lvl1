import random

import prompt


def game_calc(name):
    count = 0
    while count < 3:
        number1 = random.randint(1, 100)
        number2 = random.randint(1, 100)
        string = "+-*"
        sign = random.choice(string)
        if sign == "+":
            result = number1 + number2
        elif sign == "-":
            result = number1 - number2
        elif sign == "*":
            result = number1 * number2
        print("Question: {0} {1} {2}".format(str(number1), sign, str(number2)))
        user_answer = prompt.string("Your answer: ")
        if user_answer == str(result):
            print("Correct!")
            count += 1
        else:
            f"'{user_answer}' is wrong answer ;(. Correct answer was '{result}'.\nLet's try again, {name}!"  # noqa
            # print(
            #     "'{0}' is wrong answer ;(. Correct answer was '{1}'.\nLet's try again, {2}!".format(  # noqa
            #         user_answer, result, name
            #     )
            # )
            return
    print("Congratulations, {0}!".format(name))
