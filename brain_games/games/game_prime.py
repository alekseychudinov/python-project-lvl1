import random

from brain_games.end_answer_yes_or_no import end_answer_yes_or_no

greeting_prime = 'Answer "yes" if given number is prime. Otherwise answer "no".'

end_prime = end_answer_yes_or_no


def is_prime(number):
    d = 2
    while number % d != 0:
        d += 1
    return "yes" if d == number else "no"


def game_prime():
    number = random.randint(2, 100)
    result = is_prime(number)
    question = str(number)
    return [result, question]
