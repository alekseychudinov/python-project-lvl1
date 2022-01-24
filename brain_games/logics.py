import prompt
from brain_games.games import (
    game_calc,
    game_even,
    game_gcd,
    game_prime,
    game_progression,
)
from brain_games.greetings import greetings


def game_select(game):
    if game == "calc":
        return game_calc.game_calc
    elif game == "even":
        return game_even.game_even
    elif game == "gcd":
        return game_gcd.game_gcd
    elif game == "prime":
        return game_prime.game_prime
    elif game == "progression":
        return game_progression.game_progression


def end_of_game(game, user_answer, result, name):
    endgame = [0, ""]
    if game == "calc" or "gcd" or "progression":
        if user_answer == str(result):
            endgame[1] = "Correct!"
            endgame[0] = 1
        else:
            endgame[
                1
            ] = "'{0}' is wrong answer ;(. Correct answer was '{1}'.\nLet's try again, {2}!".format(  # noqa
                user_answer, result, name
            )
    else:
        if result == user_answer:
            endgame[1] = "Correct!"
            endgame[0] = 1
        elif result == "yes" and user_answer == "no":
            endgame[1] = (
                "'no' is wrong answer ;(. Correct answer was 'yes'.\nLet's try again, "  # noqa
                + name  # noqa
                + "!"  # noqa
            )
        elif result == "no" and user_answer == "yes":
            endgame[1] = (
                "'yes' is wrong answer ;(. Correct answer was 'no'.\nLet's try again, "  # noqa
                + name  # noqa
                + "!"  # noqa
            )
        else:
            endgame[1] = (
                "'"
                + user_answer  # noqa
                + "' is wrong answer ;(.\nLet's try again, "  # noqa
                + name  # noqa
                + "!"  # noqa
            )
    return endgame


def logics(game):
    name = greetings(game)
    game_module = game_select(game)
    count = 0
    while count < 3:
        details_of_game = game_module()
        print(details_of_game[1])
        user_answer = prompt.string("Your answer: ")
        endgame = end_of_game(game, user_answer, details_of_game[0], name)
        print(endgame[1])
        if endgame[0] == 0:
            return
        count += 1
    print("Congratulations, {0}!".format(name))
