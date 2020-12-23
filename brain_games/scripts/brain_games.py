#!/usr/bin/env python
import prompt


def main():
    print("Welcome to the Brain Games!")
    player_name = prompt.string("May I have your name? ")
    print("Hello, {}!".format(player_name))


if __name__ == "__main__":
    main()
