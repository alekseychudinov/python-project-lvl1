def end_answer_number(user_answer, result, name):
    endgame = [0, ""]
    if user_answer == str(result):
        endgame[1] = "Correct!"
        endgame[0] = 1
    else:
        endgame[
            1
        ] = "'{0}' is wrong answer ;(. Correct answer was '{1}'.\nLet's try again, {2}!".format(  # noqa
            user_answer, result, name
        )
    return endgame
