import random

GAME_WELCOME_STR = "Answer \"yes\" if the number is even, " \
                   "otherwise anser \"no\"."

START_NUM = 0
END_NUM = 65535


def generate_task():
    current_number = random.randint(START_NUM, END_NUM)
    correct_answer = "no"
    if current_number % 2 == 0:
        correct_answer = "yes"
    game_question = str(current_number)
    game_data = (game_question, correct_answer)
    return game_data
