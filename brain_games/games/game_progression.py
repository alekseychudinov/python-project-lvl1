import random

greeting = "What number is missing in the progression?"


def game_base():
    length_progression = random.randint(5, 15)
    index_of_skip_element = random.randint(0, length_progression - 1)
    step_progression = random.randint(1, 10)
    start_progression = random.randint(1, 100)
    stop_progression = start_progression + step_progression * length_progression
    progression = range(start_progression, stop_progression, step_progression)

    str_progression = ""
    counter = 0
    while counter < length_progression:
        if counter != index_of_skip_element:
            str_progression += str(progression[counter]) + " "
        else:
            str_progression += ".. "
        counter += 1
    result = progression[index_of_skip_element]
    question = str_progression
    result = str(result)
    return [result, question]
