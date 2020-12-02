#!/usr/bin/env python
import datetime
import random

GAME_WELCOME_STR = "Answer \"yes\" if given number " \
                   "is prime. Otherwise answer \"no\"."


def num_generator(start_num=0, end_num=100):
    random.seed(datetime.datetime.now())
    result = random.randint(start_num, end_num)
    return result


def odd_num_generator(start_num=0, end_num=100):
    result = num_generator(start_num, end_num)
    if result % 2 == 0:
        result = result + 1
    return result


def is_prime(num):
    divider = 2
    while num % divider != 0:
        divider = divider + 1
    return divider == num


def generate_task():
    game_data = {}
    task_number = odd_num_generator(0, 100)
    correct_answer = "no"
    if is_prime(task_number):
        correct_answer = "yes"
    game_data["game_question"] = task_number
    game_data["game_answer"] = correct_answer
    return game_data
