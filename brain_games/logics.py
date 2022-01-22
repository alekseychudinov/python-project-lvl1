from brain_games.games import (
    game_calc,
    game_even,
    game_gcd,
    game_prime,
    game_progression,
)
from brain_games.greetings import greetings


def logics(game):
    if game == "calc":
        name = greetings("What is the result of the expression?")
        game_calc.game_calc(name)
    elif game == "even":
        name = greetings(
            'Answer "yes" if the number is even, otherwise answer "no".'
        )  # noqa
        game_even.game_even(name)
    elif game == "gcd":
        name = greetings("Find the greatest common divisor of given numbers.")
        game_gcd.game_gcd(name)
    elif game == "prime":
        name = greetings(
            'Answer "yes" if given number is prime. Otherwise answer "no".'
        )
        game_prime.game_prime(name)
    elif game == "progression":
        name = greetings("What number is missing in the progression?")
        game_progression.game_progression(name)
