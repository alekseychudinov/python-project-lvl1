import math
import random

RULE = "Find the greatest common divisor of given numbers."

NUMBER_MIN = 1
NUMBER_MAX = 100


def get_correct_answer_and_question():
    number1 = random.randint(NUMBER_MIN, NUMBER_MAX)
    number2 = random.randint(NUMBER_MIN, NUMBER_MAX)
    result = math.gcd(number1, number2)
    question = "{0} {1}".format(str(number1), str(number2))
    result = str(result)
    return result, question
