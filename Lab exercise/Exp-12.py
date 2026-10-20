# Tic-Tac-Toe: Human (X) vs Computer (O)

import random

board = [" " for _ in range(9)]


def print_board():
    print()
    for i in range(0, 9, 3):
        print(f" {board[i]} | {board[i + 1]} | {board[i + 2]} ")
        if i < 6:
            print("---|---|---")
    print()


def check_winner(player):
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]

    return any(all(board[pos] == player for pos in combo)
               for combo in winning_combinations)


def is_draw():
    return " " not in board


def player_move():
    while True:
        try:
            position = int(input("Enter position (1-9): ")) - 1

            if position < 0 or position > 8:
                print("Enter a number from 1 to 9.")
            elif board[position] != " ":
                print("That position is already occupied.")
            else:
                board[position] = "X"
                break
        except ValueError:
            print("Please enter a valid number.")


def computer_move():
    empty_positions = [i for i in range(9) if board[i] == " "]
    position = random.choice(empty_positions)
    board[position] = "O"
    print(f"Computer chooses position {position + 1}")


print("Tic-Tac-Toe")
print("Positions are numbered 1 to 9:")
print(" 1 | 2 | 3 ")
print("---|---|---")
print(" 4 | 5 | 6 ")
print("---|---|---")
print(" 7 | 8 | 9 ")

while True:
    print_board()
    player_move()

    if check_winner("X"):
        print_board()
        print("You win!")
        break

    if is_draw():
        print_board()
        print("It's a draw!")
        break

    computer_move()

    if check_winner("O"):
        print_board()
        print("Computer wins!")
        break

    if is_draw():
        print_board()
        print("It's a draw!")
        break
