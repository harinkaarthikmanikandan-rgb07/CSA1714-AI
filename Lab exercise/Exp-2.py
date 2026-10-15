N = 8

def solve(board, row):
    if row == N:
        return True

    for col in range(N):
        safe = True

        for r in range(row):
            if (board[r] == col or
                abs(board[r] - col) == abs(r - row)):
                safe = False
                break

        if safe:
            board[row] = col

            if solve(board, row + 1):
                return True

    return False

board = [-1] * N

if solve(board, 0):
    for r in range(N):
        for c in range(N):
            print("Q" if board[r] == c else ".", end=" ")
        print()
else:
    print("No solution")
