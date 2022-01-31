import math
import random

RULES = "Find the greatest common divisor of given numbers."

LOWER_BOUND = 1
UPPER_BOUND = 100


def get_correct_answer_and_question():
    number1 = random.randint(LOWER_BOUND, UPPER_BOUND)
    number2 = random.randint(LOWER_BOUND, UPPER_BOUND)
    result = math.gcd(number1, number2)
    question = "{0} {1}".format(str(number1), str(number2))
    result = str(result)
    return result, question
