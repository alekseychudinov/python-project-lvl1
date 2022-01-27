import math
import random

greeting = "Find the greatest common divisor of given numbers."


def game_base():
    number1 = random.randint(1, 100)
    number2 = random.randint(1, 100)
    result = math.gcd(number1, number2)
    question = "{0} {1}".format(str(number1), str(number2))
    result = str(result)
    return [result, question]
