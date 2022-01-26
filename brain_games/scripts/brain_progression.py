#!/usr/bin/env python
from brain_games.games.game_progression import (
    end_progression,
    game_progression,
    greeting_progression,
)
from brain_games.logics import logics


def main():
    return logics(game_progression, greeting_progression, end_progression)


if __name__ == "__main__":
    main()
