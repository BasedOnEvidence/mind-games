#!/usr/bin/env python
import brain_games.cli as cli
import brain_games.games.brain_even as brain_even
import brain_games.games.brain_calc as brain_calc
import sys


def main():
    if len(sys.argv) > 1:
        current_game = sys.argv[1]
    else:
        current_game = ""
    print("Welcome to the Brain Games!")
    if current_game == "--even":
        name = cli.welcome_user()
        brain_even.even_game(name)
    elif current_game == "--calc":
        name = cli.welcome_user()
        brain_calc.calc_game(name)
    elif current_game == "--help":
        print("Here are all the arguments: ")
        print("--even - play even game")
        print("--calc - play calc game")
        print("--help - show this instructions")
    else:
        print("Type --help to find out what games you can play")


if __name__ == "__main__":
    main()
