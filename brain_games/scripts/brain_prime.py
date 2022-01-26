#!/usr/bin/env python
from brain_games.games.game_prime import end_prime, game_prime, greeting_prime
from brain_games.logics import logics


def main():
    return logics(game_prime, greeting_prime, end_prime)


if __name__ == "__main__":
    main()
