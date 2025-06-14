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
import random


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


def get_ai_move(board):
    empty_cells = [(r, c) for r in range(3)
                   for c in range(3) if board[r][c] == " "]
    return random.choice(empty_cells)


def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]

    while True:
        mode = input(
            "Play against AI or another human? Enter 'AI' or 'Human': ").strip().lower()
        if mode in ["ai", "human"]:
            break
        print("Invalid input! Please enter 'AI' or 'Human'.")

    human = "X"
    second_player = "O"
    player = human

    while True:
        print_board(board)

        if player == human or (player == second_player and mode == "human"):
            while True:
                try:
                    row, col = map(int, input(
                        f"Player {player}, enter row and column (0-2): ").split())
                    if row in range(3) and col in range(3):
                        if board[row][col] == " ":
                            break
                        else:
                            print("Cell occupied, try again!")
                    else:
                        print("Invalid input! Please enter numbers between 0 and 2.")
                except ValueError:
                    print("Invalid format! Enter two numbers separated by a space.")

        else:
            row, col = get_ai_move(board)
            print(f"AI ({second_player}) chooses: {row}, {col}")

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

        player = human if player == second_player else second_player


if __name__ == "__main__":
    tic_tac_toe()
