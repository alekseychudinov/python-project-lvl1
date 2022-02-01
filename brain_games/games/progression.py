import random

RULES = "What number is missing in the progression?"

LENGTH_MIN = 5
LENGTH_MAX = 15

COMMON_DIFFERENCE_MIN = 1
COMMON_DIFFERENCE_MAX = 10

INITIAL_TERM_MIN = 1
INITIAL_TERM_MAX = 100


def calculate_progression_terms(
    initial_term, stop_progression, common_difference
):
    progression = []
    for element in range(initial_term, stop_progression, common_difference):
        progression.append(element)
    return progression


def stringify_progression(progression, hidden_term_index):
    for index, value in enumerate(progression):
        progression[index] = str(value)
    progression[hidden_term_index] = ".."
    str_progression = " ".join(progression)
    return str_progression


def get_correct_answer_and_question():
    length_progression = random.randint(LENGTH_MIN, LENGTH_MAX)
    common_difference = random.randint(
        COMMON_DIFFERENCE_MIN, COMMON_DIFFERENCE_MAX
    )
    initial_term = random.randint(INITIAL_TERM_MIN, INITIAL_TERM_MAX)
    stop_progression = initial_term + common_difference * length_progression
    hidden_term_index = random.randint(0, length_progression - 1)

    progression = calculate_progression_terms(
        initial_term, stop_progression, common_difference
    )
    correct_answer = str(progression[hidden_term_index])
    question = stringify_progression(progression, hidden_term_index)
    return correct_answer, question
