#!/usr/bin/env python
from brain_games import cli
from brain_games import calc_functions
import prompt


def calc_game(name="Alex", total_questions=3):
    print("What is the result of the expression?")
    for _ in range(total_questions):
        game_arg1 = calc_functions.num_generator(0, 100)
        game_arg2 = calc_functions.num_generator(0, 20)
        game_oper = calc_functions.operation_generator(['+', '-', '*'])
        correct_answer = calc_functions.calculate(game_arg1,
                                                  game_arg2,
                                                  game_oper)
        print("Question: {} {} {} = ".format(game_arg1, game_oper, game_arg2))
        player_answer = prompt.string("Your answer: ")
        win_condition = cli.game_answer_check(player_answer, correct_answer)
        if not win_condition:
            break
    cli.game_result(win_condition, name)


def main():
    name = cli.welcome_user()
    calc_game(name)


if __name__ == "__main__":
    main()
