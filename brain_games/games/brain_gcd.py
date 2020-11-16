#!/usr/bin/env python
import prompt
from brain_games import calc_functions, cli


def gcd_game(name="Alex", total_questions=3):
    print("Find the greastest common divisor of given numbers.")
    for _ in range(total_questions):
        game_arg1 = calc_functions.num_generator(0, 100)
        game_arg2 = calc_functions.num_generator(0, 20)
        correct_answer = calc_functions.find_gcd(game_arg1, game_arg2)
        print("Question: {} {} = ".format(game_arg1, game_arg2))
        player_answer = prompt.string("Your answer: ")
        win_condition = cli.game_answer_check(player_answer, correct_answer)
        if not win_condition:
            break
    cli.game_result(win_condition, name)


def main():
    name = cli.welcome_user()
    gcd_game(name)


if __name__ == "__main__":
    main()
