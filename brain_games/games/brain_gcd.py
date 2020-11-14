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
    return arg1, arg2


def calculate_task(arg1, arg2):
    while arg1 != 0 and arg2 != 0:
        if arg1 > arg2:
            arg1 = arg1 % arg2
        else:
            arg2 = arg2 % arg1
    return arg1 + arg2


def gcd_game(name="Alex", total_questions=3):
    print("Find the greastest common divisor of given numbers.")
    win_condition = True
    for _ in range(total_questions):
        game_arg1, game_arg2 = generate_task()
        correct_answer = calculate_task(game_arg1, game_arg2)
        print("Question: {} {} = ".format(game_arg1, game_arg2))
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
    gcd_game(name)


if __name__ == "__main__":
    main()
