def end_answer_yes_or_no(user_answer, result, name):
    endgame = [0, ""]
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
