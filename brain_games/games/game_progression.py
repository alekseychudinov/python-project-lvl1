import random

RULE = "What number is missing in the progression?"

LENGTH_MIN = 5
LENGTH_MAX = 15

COMMON_DIFFERENCE_MIN = 1
COMMON_DIFFERENCE_MAX = 10

INITIAL_TERM_MIN = 1
INITIAL_TERM_MAX = 100


def calculation_terms_progression():
    length_progression = random.randint(LENGTH_MIN, LENGTH_MAX)
    common_difference = random.randint(
        COMMON_DIFFERENCE_MIN, COMMON_DIFFERENCE_MAX
    )
    initial_term = random.randint(INITIAL_TERM_MIN, INITIAL_TERM_MAX)
    stop_progression = initial_term + common_difference * length_progression
    progression = []
    for element in range(initial_term, stop_progression, common_difference):
        progression.append(str(element))
    return progression


def get_string_progression(progression):
    length_progression = len(progression)
    index_of_skip_element = random.randint(0, length_progression - 1)
    skip_element = progression[index_of_skip_element]
    progression[index_of_skip_element] = ".."
    str_progression = " ".join(progression)
    return skip_element, str_progression


def get_correct_answer_and_question():
    correct_answer, question = get_string_progression(
        calculation_terms_progression()
    )
    return correct_answer, question
