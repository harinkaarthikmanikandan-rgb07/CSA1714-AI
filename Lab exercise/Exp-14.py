from math import inf


def alpha_beta(state, depth, alpha, beta, maximizing, get_moves, make_move, evaluate):
    """
    Return (best_score, best_move) using minimax with alpha-beta pruning.

    get_moves(state)       -> iterable of legal moves
    make_move(state, move) -> next state
    evaluate(state)        -> score from the maximizing player's perspective
    """
    moves = list(get_moves(state))

    if depth == 0 or not moves:
        return evaluate(state), None

    best_move = None

    if maximizing:
        best_score = -inf

        for move in moves:
            next_state = make_move(state, move)
            score, _ = alpha_beta(
                next_state, depth - 1, alpha, beta, False,
                get_moves, make_move, evaluate
            )

            if score > best_score:
                best_score = score
                best_move = move

            alpha = max(alpha, best_score)
            if alpha >= beta:
                break  # Prune the remaining moves

        return best_score, best_move

    else:
        best_score = inf

        for move in moves:
            next_state = make_move(state, move)
            score, _ = alpha_beta(
                next_state, depth - 1, alpha, beta, True,
                get_moves, make_move, evaluate
            )

            if score < best_score:
                best_score = score
                best_move = move

            beta = min(beta, best_score)
            if alpha >= beta:
                break  # Prune the remaining moves

        return best_score, best_move


# Example: a simple game tree represented as a nested dictionary.
# Leaf values are scores from the maximizing player's perspective.
GAME_TREE = {
    "A": {
        "A1": {"A1a": 3, "A1b": 5},
        "A2": {"A2a": 2, "A2b": 9},
    },
    "B": {
        "B1": {"B1a": 0, "B1b": 7},
        "B2": {"B2a": 4, "B2b": 6},
    },
}


def get_moves(node):
    return list(node.keys()) if isinstance(node, dict) else []


def make_move(node, move):
    return node[move]


def evaluate(node):
    return node if isinstance(node, (int, float)) else 0


if __name__ == "__main__":
    score, move = alpha_beta(
        state=GAME_TREE,
        depth=10,
        alpha=-inf,
        beta=inf,
        maximizing=True,
        get_moves=get_moves,
        make_move=make_move,
        evaluate=evaluate,
    )

    print(f"Best move: {move}")
    print(f"Score: {score}")
