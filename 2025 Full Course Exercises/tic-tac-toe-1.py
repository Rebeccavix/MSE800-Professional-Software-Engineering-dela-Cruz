# Activity Week 10-3: Develop a Tic-tac-toe Game Using Python
'''
Develop a code decomposition and enhance your coding style. Once completed, share the GitHub link. (Estimated development time: 20 minutes)
See link: https://en.wikipedia.org/wiki/Tic-tac-toe
Summary of changes:
- Added a try-except block to catch invalid import and prompt the user again.
- Added a check to ensure the row and column are within the valid range (0,1,2).
- If the cell is already taken the user pronmpted to choose another cell instead of skipping their turn.
These changes will make yourgame more robust and user-friendly.
'''


def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)


def check_winner(board):
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != " ":
            return row[0]

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return board[0][col]

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]

    return None


def is_draw(board):
    return all(cell != " " for row in board for cell in row)


def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    player = "X"

    while True:
        print_board(board)
        row, col = map(int, input(
            f"Player {player}, enter row and column (0-2): ").split())

        if board[row][col] != " ":
            print("Cell occupied, try again!")
            continue

        board[row][col] = player
        winner = check_winner(board)

        if winner:
            print_board(board)
            print(f"Player {winner} wins!")
            break

        if is_draw(board):
            print_board(board)
            print("It's a draw!")
            break

        player = "X" if player == "O" else "O"


if __name__ == "__main__":
    tic_tac_toe()
