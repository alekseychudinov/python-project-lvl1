import prompt
from brain_games.end_of_game import end_of_game
from brain_games.greetings import greetings


def logics(game_module):
    name = greetings(game_module.greeting)
    count = 0
    while count < 3:
        details_of_game = game_module.game_base()
        print("Question: " + details_of_game[1])
        user_answer = prompt.string("Your answer: ")
        endgame = end_of_game(user_answer, details_of_game[0], name)
        print(endgame[1])
        if endgame[0] == 0:
            return
        count += 1
    print("Congratulations, {0}!".format(name))
