import random

GAME_DESCRIPTION = "Find the greatest common " \
                   "divisor of given numbers."

START_NUM = 0
END_NUM = 100


def find_gcd(arg1, arg2):
    while arg1 != 0 and arg2 != 0:
        if arg1 > arg2:
            arg1 = arg1 % arg2
        else:
            arg2 = arg2 % arg1
    return arg1 + arg2


def generate_task():
    arg1 = random.randint(START_NUM, END_NUM)
    arg2 = random.randint(START_NUM, END_NUM)
    correct_answer = find_gcd(arg1, arg2)
    game_question = "{} {}".format(arg1, arg2)
    correct_answer = str(correct_answer)
    return game_question, correct_answer
