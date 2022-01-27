import random

greeting = 'Answer "yes" if the number is even, otherwise answer "no".'


def game_base():
    number = random.randint(1, 100)
    if number % 2 == 0:
        result = "yes"
    else:
        result = "no"
    question = str(number)
    return [result, question]
