#!/usr/bin/env python
from brain_games.games.game_prime import game_prime, greeting_prime, end_prime
from brain_games.logics import logics


def main():
    return logics(game_prime, greeting_prime, end_prime)


if __name__ == "__main__":
    main()
