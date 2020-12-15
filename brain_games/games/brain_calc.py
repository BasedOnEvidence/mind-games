import random
import operator

GAME_WELCOME_STR = "What is the result of the expression?"

OPERATIONS = [(operator.add, "+"), (operator.sub, "-"), (operator.mul, "*")]

START_NUM_FOR_ARG1 = -100
END_NUM_FOR_ARG1 = 100
START_NUM_FOR_ARG2 = -10
END_NUM_FOR_ARG2 = 10


def generate_task():
    arg1 = random.randint(START_NUM_FOR_ARG1, END_NUM_FOR_ARG1)
    arg2 = random.randint(START_NUM_FOR_ARG2, END_NUM_FOR_ARG2)
    calc_function, operation = random.choice(OPERATIONS)
    correct_answer = calc_function(arg1, arg2)
    game_question = str(arg1) + " " + str(operation) + " " + str(arg2)
    game_data = (game_question, correct_answer)
    return game_data
