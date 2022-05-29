
###BOT == X ###
import math
import copy
import random

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
    xCounter = 0
    oCounter = 0

    for i in range(0, len(board)):
        for j in range(0, len(board[0])):
            if board[i][j] == X:
                xCounter += 1
            elif board[i][j] == O:
                oCounter += 1

    if xCounter > oCounter:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possibleActions = []

    for i in range(0, len(board)):
        for j in range(0, len(board[0])):
            if board[i][j] == EMPTY:
                possibleActions.append((i, j))

    return possibleActions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    # Create new board, without modifying the original board received as input
    result = copy.deepcopy(board)
    result[action[0]][action[1]] = player(board)
    return result


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Check rows
    if all(i == board[0][0] for i in board[0]):
        return board[0][0]
    elif all(i == board[1][0] for i in board[1]):
        return board[1][0]
    elif all(i == board[2][0] for i in board[2]):
        return board[2][0]
    # Check columns
    elif board[0][0] == board[1][0] and board[1][0] == board[2][0]:
        return board[0][0]
    elif board[0][1] == board[1][1] and board[1][1] == board[2][1]:
        return board[0][1]
    elif board[0][2] == board[1][2] and board[1][2] == board[2][2]:
        return board[0][2]
    # Check diagonals
    elif board[0][0] == board[1][1] and board[1][1] == board[2][2]:
        return board[0][0]
    elif board[0][2] == board[1][1] and board[1][1] == board[2][0]:
        return board[0][2]
    else:
        return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    if winner(board) is not None or (not any(EMPTY in sublist for sublist in board) and winner(board) is None):
        return True
    else:
        return False
    #return True if winner(board) is not None or (not any(EMPTY in sublist for sublist in board) and winner(board) is None) else False # noqa E501


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if terminal(board):
        if winner(board) == X:
            return 1
        elif winner(board) == O:
            return -1
        else:
            return 0
    # Check how to handle exception when a non terminal board is received.

def simulate(board):
    """
    
    simulates the game from the board condition and returns the resulting score
    
    """
    if terminal(board):
        return winner(board)
    else:
        possible_actions = actions(board)
        l = len(possible_actions)
        r = random.randint(0,l-1)
        action = possible_actions[r]
        board = result(board,action)
        return simulate(board)



# def minimax(board):
#     if terminal(board):
#         return None
#     else:
#         asshole = player(board)
#         if asshole == X:
#             whatAction,optVal = max_value(board)
#             return whatAction
#         else:
#             whatAction,optVal = min_value(board)
#             return whatAction

# def max_value(board):
#     if terminal(board):
#         return None,utility(board)
#     v = float('-inf')
#     whatAction = None
#     for action in actions(board):
#         act,val = min_value(result(copy.deepcopy(board),action))
#         if val > v:
#             v = val
#             whatAction = action
#             if v == 1:
#                 return whatAction,v
#     return whatAction , v

# def min_value(board):
#     if terminal(board):
#         return None,utility(board)
#     v = float('inf')
#     whatAction = None
#     for action in actions(board):
#         act,val = max_value(result(copy.deepcopy(board),action))
#         if val < v:
#             v = val
#             whatAction = action
#             if v == -1:
#                 return whatAction,v
#     return whatAction,v




    




    
