#!/usr/bin/env python
from brain_games import calc_functions, cli
import prompt


def prime_game(name="Alex", total_questions=3):
    print("Answer \"yes\" if given number is prime. Otherwise answer \"no\".")
    for _ in range(total_questions):
        task_number = calc_functions.odd_num_generator(0, 100)
        correct_answer = "no"
        if calc_functions.is_prime(task_number):
            correct_answer = "yes"
        print("Question: {} ".format(task_number))
        player_answer = prompt.string("Your answer: ")
        win_condition = cli.game_answer_check(player_answer, correct_answer)
        if not win_condition:
            break
    cli.game_result(win_condition, name)


def main():
    name = cli.welcome_user()
    prime_game(name)


if __name__ == "__main__":
    main()
