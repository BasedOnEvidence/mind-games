import prompt

TOTAL_QUESTIONS = 3


def run(game):
    player_name = prompt.string("May I have your name? ")
    print("Hello, {}!".format(player_name))
    print(game.GAME_DESCRIPTION)
    for _ in range(TOTAL_QUESTIONS):
        game_question, correct_answer = game.generate_task()
        print("Question: {}".format(game_question))
        player_answer = prompt.string("Your answer: ")
        if player_answer != correct_answer:
            print("'{}' is wrong answer ;(. Correct answer was '{}'.".format(
                player_answer, correct_answer
            ))
            print("Let's try again, {}!".format(player_name))
            return
        print("Correct!")
    print("Congratulations, {}".format(player_name))
