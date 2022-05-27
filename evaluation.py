from board import Board
from figures import Empty, Rook, Knight, Bishop, Queen, King, Pawn


def evaluate(board, player):
    value = 0
    for i in range(64):
        figure = board[i//8][i % 8]
        row = i//8 if player == figure.color else 7 - i//8
        colorFactor = 1 if figure.color == 'w' else -1
        value += colorFactor * (figure.value + figure.valueAdjustment[row][i % 8])

    return value


def alphaBetaMax(alpha, beta, chessBoard, color, depth, player):
    if depth == 0 or chessBoard.mated():
        return evaluate(chessBoard.board, player), (0, 0, 0, 0)
    bestmove = None
    maxval = -10**6
    if color == 'w':
        color_op = 'b'
    else:
        color_op = 'w'
    for move in chessBoard.listAllMoves(color):
        figureCaptured = chessBoard.board[move[2]][move[3]]
        figureMoved = chessBoard.board[move[0]][move[1]]
        chessBoard.board[move[0]][move[1]] = Empty()
        chessBoard.board[move[2]][move[3]] = figureMoved
        if isinstance(figureMoved, King):
            chessBoard.setKingPosition(figureMoved.color, move[2], move[3])
        score, bmove = alphaBetaMin(alpha, beta, chessBoard, color_op, depth - 1, player)
        alpha = max(score, alpha)
        if maxval <= score:
            maxval = score
            bestmove = move
        chessBoard.board[move[0]][move[1]] = figureMoved
        chessBoard.board[move[2]][move[3]] = figureCaptured
        if isinstance(figureMoved, King):
            chessBoard.setKingPosition(figureMoved.color, move[0], move[1])
        if beta <= alpha:
            break
    if bestmove == None:
        return evaluate(chessBoard.board, player), (0, 0, 0, 0)
    return maxval, bestmove






def alphaBetaMin(alpha, beta, chessBoard, color, depth, player):
    if depth == 0 or chessBoard.mated():
        return evaluate(chessBoard.board, player), (0, 0, 0, 0)
    bestmove = None
    minval = 10**6
    if color == 'w':
        color_op = 'b'
    else:
        color_op = 'w'
    for move in chessBoard.listAllMoves(color):
        figureCaptured = chessBoard.board[move[2]][move[3]]
        figureMoved = chessBoard.board[move[0]][move[1]]
        chessBoard.board[move[0]][move[1]] = Empty()
        chessBoard.board[move[2]][move[3]] = figureMoved
        if isinstance(figureMoved, King):
            chessBoard.setKingPosition(figureMoved.color, move[2], move[3])
        score, bmove = alphaBetaMax(alpha, beta, chessBoard, color_op, depth - 1, player)
        beta = min(score, beta)
        if minval >= score:
            minval = score
            bestmove = move
        chessBoard.board[move[0]][move[1]] = figureMoved
        chessBoard.board[move[2]][move[3]] = figureCaptured
        if isinstance(figureMoved, King):
            chessBoard.setKingPosition(figureMoved.color, move[0], move[1])
        if beta <= alpha:
            break
    if bestmove == None:
        return evaluate(chessBoard.board, player), (0, 0, 0, 0)
    return minval, bestmove






