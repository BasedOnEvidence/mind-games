import random

GAME_WELCOME_STR = "Answer \"yes\" if given number " \
                   "is prime. Otherwise answer \"no\"."

START_NUM = 0
END_NUM = 100


def odd_num_generator(start_num, end_num):
    result = random.randint(start_num, end_num)
    if result % 2 == 0:
        result = result + 1
    return result


def is_prime(num):
    # 1 - is not prime. %2 check, then start from 3
    if num % 2 == 0:
        return False
    divider = 3
    # If divider^2 == num - false also
    while divider * divider <= num and num % divider != 0:
        divider = divider + 2
    return divider*divider > num


def generate_task():
    task_number = odd_num_generator(START_NUM, END_NUM)
    correct_answer = "no"
    if is_prime(task_number):
        correct_answer = "yes"
    game_question = str(task_number)
    game_data = (game_question, correct_answer)
    return game_data
