import random


def game_calc():
    number1 = random.randint(1, 100)
    number2 = random.randint(1, 100)
    string = "+-*"
    sign = random.choice(string)
    result = 0
    if sign == "+":
        result = number1 + number2
    elif sign == "-":
        result = number1 - number2
    elif sign == "*":
        result = number1 * number2
    question = "Question: {0} {1} {2}".format(str(number1), sign, str(number2))
    return [result, question]
