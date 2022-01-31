import random

RULES = 'Answer "yes" if the number is even, otherwise answer "no".'

LOWER_BOUND = 1
UPPER_BOUND = 100


def is_even(number):
    return number % 2 == 0


def get_correct_answer_and_question():
    number = random.randint(LOWER_BOUND, UPPER_BOUND)
    if is_even(number):
        result = "yes"
    else:
        result = "no"
    question = str(number)
    return result, question
