import prompt


def welcome_user():
    name = prompt.string("May I have your name? ")
    print("Hello, {}!".format(name))
    return name


def game_result(win_condition, name):
    if win_condition:
        print("Congratulations, {}!".format(name))
    else:
        print("Let's try again, {}!".format(name))


def game_answer_check(player_answer, correct_answer):
    win_condition = True
    if player_answer == str(correct_answer):
        print("Correct!")
    else:
        error_text = "is wrong answer ;{. Correct answer was "
        print("\'{}\' {} \'{}\'.".format(player_answer,
                                         error_text,
                                         correct_answer))
        win_condition = False
    return win_condition


def main():
    welcome_user()


if __name__ == "__main__":
    main()
