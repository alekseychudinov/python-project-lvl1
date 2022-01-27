import random

greeting = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    d = 2
    while number % d != 0:
        d += 1
    return "yes" if d == number else "no"


def game_base():
    number = random.randint(2, 100)
    result = is_prime(number)
    question = str(number)
    return [result, question]
