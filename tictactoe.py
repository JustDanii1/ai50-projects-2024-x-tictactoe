"""
Tic Tac Toe Player
CS50 AI — Project 0

"""

import copy
import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    x_count = sum(row.count(X) for row in board)
    o_count = sum(row.count(O) for row in board)
    return X if x_count == o_count else O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    return {
        (i, j)
        for i in range(3)
        for j in range(3)
        if board[i][j] == EMPTY
    }


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    Does not mutate the original board.
    """
    i, j = action
    if i not in range(3) or j not in range(3) or board[i][j] != EMPTY:
        raise ValueError(f"Invalid action: {action}")

    new_board = copy.deepcopy(board)
    new_board[i][j] = player(board)
    return new_board


# All eight winning lines in terms (row, col)
_WIN_LINES = (
    ((0, 0), (0, 1), (0, 2)),
    ((1, 0), (1, 1), (1, 2)),
    ((2, 0), (2, 1), (2, 2)),
    ((0, 0), (1, 0), (2, 0)),
    ((0, 1), (1, 1), (2, 1)),
    ((0, 2), (1, 2), (2, 2)),
    ((0, 0), (1, 1), (2, 2)),
    ((0, 2), (1, 1), (2, 0)),
)


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for a, b, c in _WIN_LINES:
        va = board[a[0]][a[1]]
        vb = board[b[0]][b[1]]
        vc = board[c[0]][c[1]]
        if va is not EMPTY and va == vb == vc:
            return va
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True
    return all(cell != EMPTY for row in board for cell in row)


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    w = winner(board)
    if w == X:
        return 1
    if w == O:
        return -1
    return 0


# The move-ordering sequence—center, corners, sides—accelerates alpha-beta pruning,
# without changing the final minimax result
_MOVE_ORDER = [(1, 1), (0, 0), (0, 2), (2, 0), (2, 2),
               (0, 1), (1, 0), (1, 2), (2, 1)]


def _ordered_actions(board):
    return sorted(actions(board), key=_MOVE_ORDER.index)


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    Returns None if the board is a terminal state.
    """
    if terminal(board):
        return None

    current = player(board)

    def max_value(state, alpha, beta):
        if terminal(state):
            return utility(state), None
        v = -math.inf
        best_action = None
        for action in _ordered_actions(state):
            score, _ = min_value(result(state, action), alpha, beta)
            if score > v:
                v, best_action = score, action
            alpha = max(alpha, v)
            if alpha >= beta:
                break  
        return v, best_action

    def min_value(state, alpha, beta):
        if terminal(state):
            return utility(state), None
        v = math.inf
        best_action = None
        for action in _ordered_actions(state):
            score, _ = max_value(result(state, action), alpha, beta)
            if score < v:
                v, best_action = score, action
            beta = min(beta, v)
            if alpha >= beta:
                break 
        return v, best_action

    if current == X:
        _, action = max_value(board, -math.inf, math.inf)
    else:
        _, action = min_value(board, -math.inf, math.inf)
    return action
