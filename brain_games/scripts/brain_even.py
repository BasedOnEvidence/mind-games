#!/usr/bin/env python
import brain_games.cli as cli
import random
import datetime
import prompt


def even_game(name, total_questions=3):
    print("Answer \"yes\" if the number is even, otherwise anser \"no\".")
    win_condition = True
    for question_number in range(total_questions):
        random.seed(datetime.datetime.now())
        current_number = random.randint(0, 65535)
        print("Question: {}".format(current_number))
        player_answer = prompt.string("Your answer: ")
        if (((current_number % 2 == 0) and (player_answer == "yes")) or
                ((current_number % 2 != 0) and (player_answer == "no"))):
            print("Correct!")
        else:
            print("Incorrect!")
            win_condition = False
            break
    if win_condition:
        print("Congratulations, {}!".format(name))
    else:
        print("Nice try, {}!".format(name))


def main():
    name = cli.welcome_user()
    even_game(name)


if __name__ == "__main__":
    main()
