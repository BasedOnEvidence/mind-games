#!/usr/bin/env python
from brain_games import cli
from brain_games.games import brain_even, brain_calc, \
    brain_gcd, brain_progression, brain_prime
import sys


def main():
    current_game = ""
    if len(sys.argv) > 1:
        current_game = sys.argv[1]
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
    elif current_game == "--help":
        print("Here are all the arguments: ")
        print("--even - play even game")
        print("--calc - play calc game")
        print("--progression - play progression game")
        print("--prime - play prime game")
        print("--help - show this instructions")
    else:
        print("Type --help to find out what games you can play")


if __name__ == "__main__":
    main()
