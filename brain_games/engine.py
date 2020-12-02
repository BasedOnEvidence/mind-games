import prompt
from brain_games import cli

TOTAL_QUESTIONS = 3


def run(game):
    player_name = cli.welcome_user()
    win_condition = True
    print(game.GAME_WELCOME_STR)
    for _ in range(TOTAL_QUESTIONS):
        game_data = game.generate_task()
        print("Question: {}".format(game_data["game_question"]))
        player_answer = prompt.string("Your answer: ")
        if player_answer != game_data["game_answer"]:
            print("'{}' is wrong answer ;(. Coorect answer was '{}'.".format(
                player_answer, game_data["game_answer"]
            ))
            print("Let's try again, {}!".format(player_name))
            win_condition = False
            break
        print('Correct!')
    if win_condition:
        print('Congratulations, {}'.format(player_name))
