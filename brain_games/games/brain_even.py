import random

GAME_DESCRIPTION = "Answer \"yes\" if the number is even, " \
                   "otherwise anser \"no\"."

START_NUM = 0
END_NUM = 65535


def generate_task():
    current_number = random.randint(START_NUM, END_NUM)
    correct_answer = "yes" if current_number % 2 == 0 else "no"
    game_question = str(current_number)
    return game_question, correct_answer
