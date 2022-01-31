import random

RULES = "What number is missing in the progression?"

LENGTH_MIN = 5
LENGTH_MAX = 15

COMMON_DIFFERENCE_MIN = 1
COMMON_DIFFERENCE_MAX = 10

INITIAL_TERM_MIN = 1
INITIAL_TERM_MAX = 100


def progression_parameters():
    length_progression = random.randint(LENGTH_MIN, LENGTH_MAX)
    common_difference = random.randint(
        COMMON_DIFFERENCE_MIN, COMMON_DIFFERENCE_MAX
    )
    initial_term = random.randint(INITIAL_TERM_MIN, INITIAL_TERM_MAX)
    stop_progression = initial_term + common_difference * length_progression
    hidden_term_index = random.randint(0, length_progression - 1)
    return initial_term, stop_progression, common_difference, hidden_term_index


def calculate_progression_terms():
    (
        initial_term,
        stop_progression,
        common_difference,
        hidden_term_index,
    ) = progression_parameters()
    progression = []
    for element in range(initial_term, stop_progression, common_difference):
        progression.append(str(element))
    return progression, hidden_term_index


def stringify_progression():
    progression, hidden_term_index = calculate_progression_terms()
    hidden_term = progression[hidden_term_index]
    progression[hidden_term_index] = ".."
    str_progression = " ".join(progression)
    return str(hidden_term), str_progression


def get_correct_answer_and_question():
    correct_answer, question = stringify_progression()
    return correct_answer, question
