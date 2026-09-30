def display_board(board):
    cells = ["X" if cell == 1 else "O" if cell == -1 else str(i + 1) for i, cell in enumerate(board)]
    print()
    for row in range(3):
        start = row * 3
        print(f" {cells[start]} | {cells[start + 1]} | {cells[start + 2]}")
        if row < 2:
            print("---+---+---")
    print()


def get_move(board, mark):
    while True:
        try:
            position = int(input(f"{mark} move (1-9): "))
        except ValueError:
            print("Enter a number from 1 to 9.")
            continue
        except (EOFError, KeyboardInterrupt):
            print()
            return None

        if not 1 <= position <= 9:
            print("Enter a number from 1 to 9.")
        elif board[position - 1] != 0:
            print("Position is occupied.")
        else:
            return position - 1


def update_counters(position, player, rows, columns, diagonals):
    row = position // 3
    column = position % 3
    rows[row] += player
    columns[column] += player
    affected = [rows[row], columns[column]]

    if row == column:
        diagonals[0] += player
        affected.append(diagonals[0])
    if row + column == 2:
        diagonals[1] += player
        affected.append(diagonals[1])

    return 3 in affected or -3 in affected


def play_game():
    board = [0] * 9
    rows = [0] * 3
    columns = [0] * 3
    diagonals = [0] * 2
    player = 1

    for _ in range(9):
        display_board(board)
        mark = "X" if player == 1 else "O"
        position = get_move(board, mark)
        if position is None:
            return False

        board[position] = player
        if update_counters(position, player, rows, columns, diagonals):
            display_board(board)
            print(f"{mark} wins.")
            return True

        player = -player

    display_board(board)
    print("Draw.")
    return True


def play_again():
    while True:
        try:
            answer = input("Play again? (y/n): ").strip().lower()
        except (EOFError, KeyboardInterrupt):
            print()
            return False

        if answer in ("y", "yes"):
            return True
        if answer in ("n", "no"):
            return False
        print("Enter y or n.")


def main():
    while play_game():
        if not play_again():
            break


if __name__ == "__main__":
    main()
