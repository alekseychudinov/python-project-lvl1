import math
import random


def game_gcd():
    number1 = random.randint(1, 100)
    number2 = random.randint(1, 100)
    result = math.gcd(number1, number2)
    question = "Question: {0} {1}".format(str(number1), str(number2))
    return [result, question]
