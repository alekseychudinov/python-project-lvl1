import prompt

NUMBER_OF_ROUNDS = 3


def run(game):
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print("Hello, {0}!".format(name))
    print(game.RULES)

    count = 0
    while count < NUMBER_OF_ROUNDS:
        correct_answer, question = game.get_correct_answer_and_question()
        print("Question: " + question)
        user_answer = prompt.string("Your answer: ")

        if correct_answer == user_answer:
            print("Correct!")
            count += 1
        else:
            print(
                "'{0}' is wrong answer ;(. Correct answer was '{1}'.\nLet's try again, {2}!".format(  # noqa
                    user_answer, correct_answer, name
                )
            )
            return

    print("Congratulations, {0}!".format(name))
