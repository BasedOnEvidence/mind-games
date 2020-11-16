#!/usr/bin/env python
import sys
from brain_games import cli
from brain_games.games import (
    brain_even,
    brain_calc,
    brain_gcd,
    brain_progression,
    brain_prime,
)


def game_selection(current_game):
    print("Welcome to the Brain Games!")
    if current_game == "--even":
        name = cli.welcome_user()
        brain_even.even_game(name)
    elif current_game == "--calc":
        name = cli.welcome_user()
        brain_calc.calc_game(name)
    elif current_game == "--gcd":
        name = cli.welcome_user()
        brain_gcd.gcd_game(name)
    elif current_game == "--progression":
        name = cli.welcome_user()
        brain_progression.progression_game(name)
    elif current_game == "--prime":
        name = cli.welcome_user()
        brain_prime.prime_game(name)
    else:
        print("Here are all the arguments, choose your game!")
        print("--even - play even game")
        print("--calc - play calc game")
        print("--gcd - play gcd game")
        print("--progression - play progression game")
        print("--prime - play prime game")


def main():
    current_game = ""
    if len(sys.argv) > 1:
        current_game = sys.argv[1]
    game_selection(current_game)


if __name__ == "__main__":
    main()
