import random

GAME_WELCOME_STR = "Answer \"yes\" if given number " \
                   "is prime. Otherwise answer \"no\"."

START_NUM = 1
END_NUM = 101
STEP = 2


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
    task_number = random.randrange(START_NUM, END_NUM, STEP)
    correct_answer = "no"
    if is_prime(task_number):
        correct_answer = "yes"
    game_question = str(task_number)
    game_data = (game_question, correct_answer)
    return game_data
