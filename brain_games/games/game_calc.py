import random

greeting = "What is the result of the expression?"


def game_base():
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
    question = "{0} {1} {2}".format(str(number1), sign, str(number2))
    result = str(result)
    return [result, question]
