import random

RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'

NUMBER_MIN = 2
NUMBER_MAX = 100


def is_prime(number):
    d = 2
    while number % d != 0:
        d += 1
    return True if d == number else False


def get_correct_answer_and_question():
    number = random.randint(NUMBER_MIN, NUMBER_MAX)
    if is_prime(number):
        result = "yes"
    else:
        result = "no"
    question = str(number)
    return result, question
