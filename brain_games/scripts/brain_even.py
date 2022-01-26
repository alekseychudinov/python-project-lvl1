#!/usr/bin/env python
from brain_games.games.game_even import end_even, game_even, greeting_even
from brain_games.logics import logics


def main():
    return logics(game_even, greeting_even, end_even)


if __name__ == "__main__":
    main()
