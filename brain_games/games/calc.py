import random

RULES = "What is the result of the expression?"

LOWER_BOUND = 1
UPPER_BOUND = 100


def get_correct_answer_and_question():
    number1 = random.randint(LOWER_BOUND, UPPER_BOUND)
    number2 = random.randint(LOWER_BOUND, UPPER_BOUND)
    sign_options = "+-*"
    sign = random.choice(sign_options)
    result = 0
    if sign == "+":
        result = number1 + number2
    elif sign == "-":
        result = number1 - number2
    elif sign == "*":
        result = number1 * number2
    question = "{0} {1} {2}".format(str(number1), sign, str(number2))
    result = str(result)
    return result, question
