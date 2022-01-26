import random

from brain_games.end_answer_yes_or_no import end_answer_yes_or_no

greeting_even = 'Answer "yes" if the number is even, otherwise answer "no".'

end_even = end_answer_yes_or_no


def game_even():
    number = random.randint(1, 100)
    if number % 2 == 0:
        result = "yes"
    else:
        result = "no"
    question = str(number)
    return [result, question]
