#!/usr/bin/env python
from brain_games import cli
from brain_games import calc_functions
import prompt


def generate_task(progression_len, hide_num, start_num, increment):
    task_str = str(start_num) + ' '
    new_elem = start_num
    if hide_num == 0:
        task_str = ".. "
        correct_answer = start_num
    for elem_num in range(1, progression_len):
        new_elem = new_elem + increment
        if hide_num == elem_num:
            task_str = task_str + ".. "
            correct_answer = new_elem
        else:
            task_str = task_str + str(new_elem) + ' '
    return task_str, correct_answer


def progression_game(name="Alex", total_questions=3):
    print("What number is missing in the progression?")
    for _ in range(total_questions):
        progression_len = calc_functions.num_generator(5, 10)
        hide_num = calc_functions.num_generator(0, progression_len-1)
        start_num = calc_functions.num_generator(0, 20)
        increment = calc_functions.num_generator(1, 10)
        task_str, correct_answer = generate_task(progression_len,
                                                 hide_num,
                                                 start_num,
                                                 increment)
        print("Question: {} ".format(task_str))
        player_answer = prompt.string("Your answer: ")
        win_condition = cli.game_answer_check(player_answer, correct_answer)
        if not win_condition:
            break
    cli.game_result(win_condition, name)


def main():
    name = cli.welcome_user()
    progression_game(name)


if __name__ == "__main__":
    main()
