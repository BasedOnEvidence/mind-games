import datetime
import random

GAME_WELCOME_STR = "What number is missing " \
                   "in the progression?"


def num_generator(start_num=0, end_num=100):
    random.seed(datetime.datetime.now())
    result = random.randint(start_num, end_num)
    return result


def generate_data(progression_len, hide_num, start_num, increment):
    task_str = str(start_num) + " "
    new_elem = start_num
    if hide_num == 0:
        task_str = ".. "
        correct_answer = start_num
    for elem_num in range(1, progression_len):
        new_elem = new_elem + increment
        if hide_num == elem_num:
            task_str = task_str + ".. "
            correct_answer = new_elem
        else:
            task_str = task_str + str(new_elem) + " "
    return task_str, correct_answer


def generate_task():
    game_data = {}
    progression_len = num_generator(5, 10)
    hide_num = num_generator(0, progression_len - 1)
    start_num = num_generator(0, 20)
    increment = num_generator(1, 10)
    task_str, correct_answer = generate_data(
        progression_len, hide_num, start_num, increment
    )
    game_data["game_question"] = task_str
    game_data["game_answer"] = str(correct_answer)
    return game_data
