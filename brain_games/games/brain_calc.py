#!/usr/bin/env python
import datetime
import random

GAME_WELCOME_STR = "What is the result of the expression?"


def operation_generator(operations_list):
    random.seed(datetime.datetime.now())
    operation = operations_list[random.randint(0, len(operations_list) - 1)]
    return operation


def calculate(arg1, arg2, operation):
    result = 0
    if operation == "+":
        result = arg1 + arg2
    if operation == "-":
        result = arg1 - arg2
    if operation == "*":
        result = arg1 * arg2
    return result


def num_generator(start_num=0, end_num=100):
    random.seed(datetime.datetime.now())
    result = random.randint(start_num, end_num)
    return result


def generate_task():
    game_data = {}
    arg1 = num_generator(0, 100)
    arg2 = num_generator(0, 20)
    operation = operation_generator(["+", "-", "*"])
    correct_answer = calculate(arg1, arg2, operation)
    game_data["game_question"] = str(arg1) + " " + str(operation)
    game_data["game_question"] += " " + str(arg2)
    game_data["game_answer"] = str(correct_answer)
    return game_data
