import random

from brain_games.is_prime import is_prime


def game_prime():
    number = random.randint(2, 100)
    result = is_prime(number)
    question = "Question: " + str(number)
    return [result, question]
