#!/usr/bin/env python
from brain_games.games.game_calc import game_calc, greeting_calc, end_calc
from brain_games.logics import logics


def main():
    return logics(game_calc, greeting_calc, end_calc)


if __name__ == "__main__":
    main()
