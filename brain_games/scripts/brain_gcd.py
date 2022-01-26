#!/usr/bin/env python
from brain_games.games.game_gcd import game_gcd, greeting_gcd, end_gcd
from brain_games.logics import logics


def main():
    return logics(game_gcd, greeting_gcd, end_gcd)


if __name__ == "__main__":
    main()
