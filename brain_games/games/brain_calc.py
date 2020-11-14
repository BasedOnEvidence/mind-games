#!/usr/bin/env python
import brain_games.cli as cli
import random
import datetime
import prompt


def generate_task():
    random.seed(datetime.datetime.now())
    arg1 = random.randint(0, 100)
    random.seed(datetime.datetime.now())
    arg2 = random.randint(0, 100)
    operations_list = ['+', '-', '*']
    random.seed(datetime.datetime.now())
    operation = operations_list[random.randint(0, len(operations_list)-1)]
    return arg1, arg2, operation


def calculate_task(arg1, arg2, operation):
    result = ''
    if operation == '+':
        result = arg1 + arg2
    if operation == '-':
        result = arg1 - arg2
    if operation == '*':
        result = arg1 * arg2
    return result


def calc_game(name="Alex", total_questions=3):
    print("What is the result of the expression?")
    win_condition = True
    for question_number in range(total_questions):
        game_arg1, game_arg2, game_oper = generate_task()
        correct_answer = calculate_task(game_arg1, game_arg2, game_oper)
        print("Question: {} {} {} = ".format(game_arg1, game_oper, game_arg2))
        player_answer = prompt.string("Your answer: ")
        if int(player_answer) == correct_answer:
            print("Correct!")
        else:
            error_text = "is wrong answer ;{. Correct answer was "
            print("\'{}\' {} \'{}\'.".format(player_answer,
                                             error_text,
                                             correct_answer))
            win_condition = False
            break
    if win_condition:
        print("Congratulations, {}!".format(name))
    else:
        print("Let's try again, {}!".format(name))


def main():
    name = cli.welcome_user()
    calc_game(name)


if __name__ == "__main__":
    main()
