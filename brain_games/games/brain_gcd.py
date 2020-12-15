import random

GAME_WELCOME_STR = "Find the greatest common " \
                   "divisor of given numbers."

START_NUM_FOR_ARG1 = 0
END_NUM_FOR_ARG1 = 100
START_NUM_FOR_ARG2 = 0
END_NUM_FOR_ARG2 = 20


def find_gcd(arg1, arg2):
    while arg1 != 0 and arg2 != 0:
        if arg1 > arg2:
            arg1 = arg1 % arg2
        else:
            arg2 = arg2 % arg1
    return arg1 + arg2


def generate_task():
    arg1 = random.randint(START_NUM_FOR_ARG1, END_NUM_FOR_ARG1)
    arg2 = random.randint(START_NUM_FOR_ARG2, END_NUM_FOR_ARG2)
    correct_answer = find_gcd(arg1, arg2)
    game_question = str(arg1) + " " + str(arg2)
    correct_answer = str(correct_answer)
    game_data = (game_question, correct_answer)
    return game_data
