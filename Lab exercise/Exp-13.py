def print_board(board):
    print()
    for row in range(3):
        print(" " + " | ".join(board[row * 3:row * 3 + 3]))
        if row < 2:
            print("---+---+---")
    print()


def check_winner(board):
    lines = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
        (0, 4, 8), (2, 4, 6)              # Diagonals
    ]

    for a, b, c in lines:
        if board[a] == board[b] == board[c] and board[a] != " ":
            return board[a]

    return None


def minimax(board, is_maximizing):
    winner = check_winner(board)

    if winner == "O":
        return 1
    if winner == "X":
        return -1
    if " " not in board:
        return 0

    if is_maximizing:
        best_score = -float("inf")

        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(board, False)
                board[i] = " "
                best_score = max(best_score, score)

        return best_score

    best_score = float("inf")

    for i in range(9):
        if board[i] == " ":
            board[i] = "X"
            score = minimax(board, True)
            board[i] = " "
            best_score = min(best_score, score)

    return best_score


def computer_move(board):
    best_score = -float("inf")
    move = None

    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(board, False)
            board[i] = " "

            if score > best_score:
                best_score = score
                move = i

    return move


def main():
    board = [" "] * 9
    print("You are X. The computer is O.")
    print("Choose a square from 1 to 9:")

    while True:
        print_board(board)

        # Get the player's move
        try:
            position = int(input("Your move (1-9): ")) - 1
        except ValueError:
            print("Please enter a number.")
            continue

        if position < 0 or position > 8 or board[position] != " ":
            print("That square is unavailable. Try again.")
            continue

        board[position] = "X"

        if check_winner(board) == "X":
            print_board(board)
            print("You win!")
            break

        if " " not in board:
            print_board(board)
            print("It's a draw!")
            break

        # Computer's move
        position = computer_move(board)
        board[position] = "O"
        print("Computer chooses square", position + 1)

        if check_winner(board) == "O":
            print_board(board)
            print("Computer wins!")
            break

        if " " not in board:
            print_board(board)
            print("It's a draw!")
            break


main()
