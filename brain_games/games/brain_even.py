#!/usr/bin/env python
import prompt
from brain_games import calc_functions, cli


def even_game(name="Alex", total_questions=3):
    print('Answer "yes" if the number is even, otherwise anser "no".')
    for _ in range(total_questions):
        current_number = calc_functions.num_generator(0, 65535)
        print("Question: {}".format(current_number))
        correct_answer = "no"
        if current_number % 2 == 0:
            correct_answer = "yes"
        player_answer = prompt.string("Your answer: ")
        win_condition = cli.game_answer_check(player_answer, correct_answer)
        if not win_condition:
            break
    cli.game_result(win_condition, name)


def main():
    name = cli.welcome_user()
    even_game(name)


if __name__ == "__main__":
    main()
