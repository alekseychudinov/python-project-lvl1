import random

RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'

LOWER_BOUND = 2
UPPER_BOUND = 100


def is_prime(number):
    d = 2
    while number % d != 0:
        d += 1
    return d == number


def get_correct_answer_and_question():
    number = random.randint(LOWER_BOUND, UPPER_BOUND)
    if is_prime(number):
        result = "yes"
    else:
        result = "no"
    question = str(number)
    return result, question
