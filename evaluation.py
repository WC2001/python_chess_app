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
        e = evaluate(chessBoard.board, player)
        return e, (0, 0), (0, 0)
    bestmove = None
    maxval = -10**6
    beststart = (-1, -1)
    if color == 'w':
        color_op = 'b'
    else:
        color_op = 'w'
    for i in range(64):
        if chessBoard.board[i//8][i % 8].color != color:
            pass
        else:
            for move in chessBoard.list_possible_moves(i//8, i % 8):
                figureCaptured = chessBoard.board[move[0]][move[1]]
                figureMoved = chessBoard.board[i // 8][i % 8]
                chessBoard.board[i // 8][i % 8] = Empty()
                chessBoard.board[move[0]][move[1]] = figureMoved
                if isinstance(figureMoved, King):
                    chessBoard.setKingPosition(figureMoved.color, move[0], move[1])
                score, bmove, bstart = alphaBetaMin(alpha, beta, chessBoard, color_op, depth - 1, player)
                alpha = max(score, alpha)
                if maxval <= score:
                    maxval = score
                    bestmove = move
                    beststart = (i // 8, i % 8)
                chessBoard.board[i // 8][i % 8] = figureMoved
                chessBoard.board[move[0]][move[1]] = figureCaptured
                if isinstance(figureMoved, King):
                    chessBoard.setKingPosition(figureMoved.color, i // 8, i % 8)
                if beta <= alpha:
                    break

    return maxval, bestmove, beststart


def alphaBetaMin(alpha, beta, chessBoard, color, depth, player):
    if depth == 0 or chessBoard.mated():
        e = evaluate(chessBoard.board, player)
        return e, (0, 0), (0, 0)
    bestmove = None
    minval = 10**6
    beststart = (-1, -1)
    if color == 'w':
        color_op = 'b'
    else:
        color_op = 'w'
    for i in range(64):
        if chessBoard.board[i//8][i%8].color != color:
            pass
        else:
            for move in chessBoard.list_possible_moves(i//8, i % 8):
                figureCaptured = chessBoard.board[move[0]][move[1]]
                figureMoved = chessBoard.board[i // 8][i % 8]
                chessBoard.board[i // 8][i % 8] = Empty()
                chessBoard.board[move[0]][move[1]] = figureMoved
                if isinstance(figureMoved, King):
                    chessBoard.setKingPosition(figureMoved.color, move[0], move[1])
                score, bmove, bstart = alphaBetaMax(alpha, beta, chessBoard, color_op, depth - 1, player)
                beta = min(score, beta)
                if score <= minval:
                    minval = score
                    bestmove = move
                    beststart = (i // 8, i % 8)
                if isinstance(figureMoved, King):
                    chessBoard.setKingPosition(figureMoved.color, i//8, i % 8)
                chessBoard.board[i // 8][i % 8] = figureMoved
                chessBoard.board[move[0]][move[1]] = figureCaptured

                if beta <= alpha:
                    break
    return minval, bestmove, beststart




