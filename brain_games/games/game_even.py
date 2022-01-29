import random

RULE = 'Answer "yes" if the number is even, otherwise answer "no".'

NUMBER_MIN = 1
NUMBER_MAX = 100


def is_even(number):
    return True if number % 2 == 0 else False


def get_correct_answer_and_question():
    number = random.randint(NUMBER_MIN, NUMBER_MAX)
    if is_even(number):
        result = "yes"
    else:
        result = "no"
    question = str(number)
    return result, question
