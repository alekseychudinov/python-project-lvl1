import random


def game_even():
    number = random.randint(1, 100)
    if number % 2 == 0:
        result = "yes"
    else:
        result = "no"
    question = "Question: " + str(number)
    return [result, question]
