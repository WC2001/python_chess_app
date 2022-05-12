import time

from board import Board
from figures import Empty, Rook, Knight, Bishop, Queen, King, Pawn


def evaluate(board, color):
    value = 0
    for i in range(64):
        row = i//8 if color == 'w' else 7 - i//8
        colorFactor = 1 if board[i//8][i % 8].color == 'w' else -1
        value += colorFactor * (board[i//8][i % 8].value + board[i//8][i % 8].valueAdjustment[row][i % 8])

    return value


def alphaBetaMax(alpha, beta, chessBoard, color, depth):
    if depth == 0 or not chessBoard.can_move("w") or not chessBoard.can_move('b'):
        e = evaluate(chessBoard.board, color)
        return e, ((0, 0), (0, 0))
    bestmove = None
    maxval = -10**6
    if color == 'w':
        color_op = 'b'
    else:
        color_op = 'w'
    moves = chessBoard.getAllMoves(color)
    # moves = moveOrdering(moves, chessBoard.board)
    for move in moves:
        start = move[0]
        target = move[1]
        figureCaptured = chessBoard.board[target[0]][target[1]]
        # chessBoard.move(i // 8, i % 8, move[0], move[1])
        figureMoved = chessBoard.board[start[0]][start[1]]
        chessBoard.board[start[0]][start[1]] = Empty()
        chessBoard.board[target[0]][target[1]] = figureMoved
        if isinstance(figureMoved, King):
            chessBoard.setKingPosition(figureMoved.color, target[0], target[1])
        score, bmove = alphaBetaMin(alpha, beta, chessBoard, color_op, depth - 1)
        alpha = max(score, alpha)
        if maxval <= score:
            maxval = score
            bestmove = move
            # beststart = (i // 8, i % 8)
        chessBoard.board[start[0]][start[1]] = figureMoved
        chessBoard.board[target[0]][target[1]] = figureCaptured
        if isinstance(figureMoved, King):
            chessBoard.setKingPosition(figureMoved.color, start[0], start[1])
        # chessBoard.unmove(move[0], move[1], i // 8, i % 8, figureCaptured)
        if beta <= alpha:
            break
    # for i in range(64):
    #     # print(alpha, beta)
    #     if chessBoard.board[i//8][i % 8].color != color:
    #         pass
    #     else:
    #         moves = chessBoard.list_possible_moves(i//8, i % 8)
    #         moves = moveOrdering(moves, chessBoard.board, i//8, i%8)
    #         for move in moves:
    #             figureCaptured = chessBoard.board[move[0]][move[1]]
    #             # chessBoard.move(i // 8, i % 8, move[0], move[1])
    #             figureMoved = chessBoard.board[i // 8][i % 8]
    #             chessBoard.board[i // 8][i % 8] = Empty()
    #             chessBoard.board[move[0]][move[1]] = figureMoved
    #             if isinstance(figureMoved, King):
    #                 chessBoard.setKingPosition(figureMoved.color, move[0], move[1])
    #             score, bmove, bstart = alphaBetaMin(alpha, beta, chessBoard, color_op, depth - 1)
    #             alpha = max(score, alpha)
    #             if maxval <= score:
    #                 maxval = score
    #                 bestmove = move
    #                 beststart = (i // 8, i % 8)
    #             chessBoard.board[i // 8][i % 8] = figureMoved
    #             chessBoard.board[move[0]][move[1]] = figureCaptured
    #             if isinstance(figureMoved, King):
    #                 chessBoard.setKingPosition(figureMoved.color, i // 8, i % 8)
    #             # chessBoard.unmove(move[0], move[1], i // 8, i % 8, figureCaptured)
    #             if beta <= alpha:
    #                 break

    return maxval, bestmove


def alphaBetaMin(alpha, beta, chessBoard, color, depth):
    if depth == 0 or not chessBoard.can_move("w") or not chessBoard.can_move('b'):
        e = evaluate(chessBoard.board, color)
        return e, ((0, 0), (0, 0))
    bestmove = None
    minval = 10**6
    beststart = (-1, -1)
    if color == 'w':
        color_op = 'b'
    else:
        color_op = 'w'
    moves = chessBoard.getAllMoves(color)
    # moves = moveOrdering(moves, chessBoard.board)
    for move in moves:
        start = move[0]
        target = move[1]
        figureCaptured = chessBoard.board[target[0]][target[1]]
        # chessBoard.move(i // 8, i % 8, move[0], move[1])
        figureMoved = chessBoard.board[start[0]][start[1]]
        chessBoard.board[start[0]][start[1]] = Empty()
        chessBoard.board[target[0]][target[1]] = figureMoved
        if isinstance(figureMoved, King):
            chessBoard.setKingPosition(figureMoved.color, target[0], target[1])
        score, bmove = alphaBetaMax(alpha, beta, chessBoard, color_op, depth - 1)
        beta = min(score, beta)
        if minval >= score:
            minval = score
            bestmove = move
            # beststart = (i // 8, i % 8)
        chessBoard.board[start[0]][start[1]] = figureMoved
        chessBoard.board[target[0]][target[1]] = figureCaptured
        if isinstance(figureMoved, King):
            chessBoard.setKingPosition(figureMoved.color, start[0], start[1])
        # chessBoard.unmove(move[0], move[1], i // 8, i % 8, figureCaptured)
        if beta <= alpha:
            break
    # for i in range(64):
    #     # print(alpha, beta)
    #     if chessBoard.board[i//8][i%8].color != color:
    #         pass
    #     else:
    #         moves = chessBoard.list_possible_moves(i // 8, i % 8)
    #         moves = moveOrdering(moves, chessBoard.board, i // 8, i % 8)
    #         for move in moves:
    #             # chessBoard.move(i//8, i % 8, move[0], move[1])
    #             figureCaptured = chessBoard.board[move[0]][move[1]]
    #             figureMoved = chessBoard.board[i // 8][i % 8]
    #             figureCaptured = chessBoard.board[move[0]][move[1]]
    #             chessBoard.board[i // 8][i % 8] = Empty()
    #             chessBoard.board[move[0]][move[1]] = figureMoved
    #             if isinstance(figureMoved, King):
    #                 chessBoard.setKingPosition(figureMoved.color, move[0], move[1])
    #             score, bmove, bstart = alphaBetaMax(alpha, beta, chessBoard, color_op, depth - 1)
    #             beta = min(score, beta)
    #             if score <= minval:
    #                 minval = score
    #                 bestmove = move
    #                 beststart = (i // 8, i % 8)
    #             # chessBoard.unmove(move[0], move[1], i//8, i % 8, figureCaptured)
    #             if isinstance(figureMoved, King):
    #                 chessBoard.setKingPosition(figureMoved.color, i//8, i % 8)
    #             chessBoard.board[i // 8][i % 8] = figureMoved
    #             chessBoard.board[move[0]][move[1]] = figureCaptured
    #
    #             if beta <= alpha:
    #                 break
    return minval, bestmove


# def moveOrdering(moves, board, x, y):
#     def moveScore(move1):
#         attackerValue = board[x][y].value
#         target1Value = board[move1[0]][move1[1]].value
#         return (10 * target1Value - attackerValue)
#     return sorted(moves, key=moveScore, reverse=True)

def moveOrdering(moves, board):
    def moveScore(move):
        start = move[0]
        target = move[1]
        attackerValue = board[start[0]][start[1]].value
        targetValue = board[target[0]][target[1]].value
        return (10 * targetValue - attackerValue)
    return sorted(moves, key=moveScore, reverse=True)



# if __name__ == "__main__":
#
#     chessBoard = Board([], (7, 4), (0, 4))
#     chessBoard.w_king_pos = (7, 4)
#     chessBoard.b_king_pos = (0, 4)
#     chessBoard.board = [[Rook('b'), Knight('b'), Bishop('b'), Queen('b'), King('b'), Bishop('b'), Knight('b'), Rook('b')],
#                         [Pawn('b'), Pawn('b'), Pawn('b'), Pawn('b'), Pawn('b'), Pawn('b'), Empty(), Pawn('b')],
#                         [Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty()],
#                         [Empty(), Empty(), Empty(), Queen('b'), Empty(), Empty(), Empty(), Empty()],
#                         [Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty()],
#                         [Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty()],
#                         [Pawn('w'), Pawn('w'), Pawn('w'), Empty(), Pawn('w'), Pawn('w'), Pawn('w'), Pawn('w')],
#                         [Rook('w'), Knight('w'), Bishop('w'), Queen('w'), King('w'), Bishop('w'), Knight('w'),
#                          Rook('w')]
#                         ]
#     start = time.time()
#     s, m, st = alphaBetaMax(-100000, 100000, chessBoard, 'w', 4)
#     print(time.time() - start)
#     print(s)
#     print(st)
#     print(m)



