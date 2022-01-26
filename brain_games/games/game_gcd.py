import math
import random

from brain_games.end_answer_number import end_answer_number

greeting_gcd = "Find the greatest common divisor of given numbers."

end_gcd = end_answer_number


def game_gcd():
    number1 = random.randint(1, 100)
    number2 = random.randint(1, 100)
    result = math.gcd(number1, number2)
    question = "{0} {1}".format(str(number1), str(number2))
    return [result, question]
