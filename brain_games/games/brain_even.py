#!/usr/bin/env python
import datetime
import random

GAME_WELCOME_STR = "Answer \"yes\" if the number is even, " \
                   "otherwise anser \"no\"."


def num_generator(start_num=0, end_num=100):
    random.seed(datetime.datetime.now())
    result = random.randint(start_num, end_num)
    return result


def generate_task():
    game_data = {}
    current_number = num_generator(0, 65535)
    correct_answer = "no"
    if current_number % 2 == 0:
        correct_answer = "yes"
    game_data["game_question"] = current_number
    game_data["game_answer"] = correct_answer
    return game_data
