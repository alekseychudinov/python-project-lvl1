import prompt

NUMBER_OF_ROUNDS = 3


def move(module_game):
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print("Hello, {0}!".format(name))
    print(module_game.RULE)

    count = 0
    while count < NUMBER_OF_ROUNDS:
        correct_answer, question = module_game.get_correct_answer_and_question()
        print("Question: " + question)
        user_answer = prompt.string("Your answer: ")

        endgame = [0, ""]
        if correct_answer == user_answer:
            endgame[1] = "Correct!"
            endgame[0] = 1
        else:
            endgame[
                1
            ] = "'{0}' is wrong answer ;(. Correct answer was '{1}'.\nLet's try again, {2}!".format(  # noqa
                user_answer, correct_answer, name
            )

        print(endgame[1])
        if endgame[0] == 0:
            return
        count += 1

    print("Congratulations, {0}!".format(name))
