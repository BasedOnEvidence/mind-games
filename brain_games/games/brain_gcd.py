#!/usr/bin/env python
import datetime
import random

GAME_WELCOME_STR = "Find the greatest common " \
                   "divisor of given numbers."


def num_generator(start_num=0, end_num=100):
    random.seed(datetime.datetime.now())
    result = random.randint(start_num, end_num)
    return result


def find_gcd(arg1, arg2):
    while arg1 != 0 and arg2 != 0:
        if arg1 > arg2:
            arg1 = arg1 % arg2
        else:
            arg2 = arg2 % arg1
    return arg1 + arg2


def generate_task():
    game_data = {}
    arg1 = num_generator(0, 100)
    arg2 = num_generator(0, 20)
    correct_answer = find_gcd(arg1, arg2)
    game_data["game_question"] = str(arg1) + " " + str(arg2)
    game_data["game_answer"] = str(correct_answer)
    return game_data
