import random

GAME_DESCRIPTION = "Answer \"yes\" if given number " \
                   "is prime. Otherwise answer \"no\"."

START_NUM = 1
END_NUM = 101
STEP = 2


def is_prime(num):
    # 1 - is not prime. %2 check, then start from 3
    if num <= 1:
        return False
    divider = 3
    # If divider^2 == num - false also
    while divider * divider <= num and num % divider != 0:
        divider = divider + 2
    return divider * divider > num


def generate_task():
    number = random.randrange(START_NUM, END_NUM, STEP)
    correct_answer = "yes" if is_prime(number) else "no"
    game_question = str(number)
    return game_question, correct_answer
