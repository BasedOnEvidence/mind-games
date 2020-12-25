import random

GAME_DESCRIPTION = "What number is missing " \
                   "in the progression?"

START_MIN = 0
START_MAX = 20
INC_MIN = 1
INC_MAX = 10
PROGRESSION_LEN_MIN = 5
PROGRESSION_LEN_MAX = 10


def generate_task():
    progression_len = random.randint(PROGRESSION_LEN_MIN, PROGRESSION_LEN_MAX)
    hidden_index = random.randint(0, progression_len - 1)
    start_num = random.randint(START_MIN, START_MAX)
    increment = random.randint(INC_MIN, INC_MAX)
    progression = [
        str(start_num + i * increment)
        for i in range(progression_len)
    ]
    correct_answer = progression[hidden_index]
    progression[hidden_index] = ".."
    game_question = " ".join(progression)
    return game_question, correct_answer
