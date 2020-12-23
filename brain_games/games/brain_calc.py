import random
import operator

GAME_DESCRIPTION = "What is the result of the expression?"

OPERATIONS = [(operator.add, "+"), (operator.sub, "-"), (operator.mul, "*")]

START_NUM = -100
END_NUM = 100


def generate_task():
    arg1 = random.randint(START_NUM, END_NUM)
    arg2 = random.randint(START_NUM, END_NUM)
    calc_function, operation = random.choice(OPERATIONS)
    correct_answer = calc_function(arg1, arg2)
    game_question = "{} {} {}".format(arg1, operation, arg2)
    return game_question, correct_answer
