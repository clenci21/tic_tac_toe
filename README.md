# Tic-Tac-Toe

A two-player Tic-Tac-Toe game that runs in the terminal. The project is mainly an algorithms experiment, using a compact counter-based approach instead of checking every possible winning combination on a 3x3 matrix.

Run it with:

```sh
python main.py
```

The board is stored as nine cells using `1` for X, `-1` for O, and `0` for an empty position. Three row counters, three column counters, and two diagonal counters are updated after each move. Only the counters affected by that move are checked, and a value of `3` or `-3` means that player has won. This makes the win detection the more interesting part of the project rather than the game itself.
