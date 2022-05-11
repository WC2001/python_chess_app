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
        return e, (0, 0), (0, 0)
    bestmove = None
    maxval = -10**6
    beststart = (-1, -1)
    if color == 'w':
        color_op = 'b'
    else:
        color_op = 'w'
    for i in range(64):
        # print(alpha, beta)
        if chessBoard.board[i//8][i % 8].color != color:
            pass
        else:
            for move in chessBoard.list_possible_moves(i//8, i % 8):
                figureCaptured = chessBoard.board[move[0]][move[1]]
                # chessBoard.move(i // 8, i % 8, move[0], move[1])
                figureMoved = chessBoard.board[i // 8][i % 8]
                chessBoard.board[i // 8][i % 8] = Empty()
                chessBoard.board[move[0]][move[1]] = figureMoved
                if isinstance(figureMoved, King):
                    chessBoard.setKingPosition(figureMoved.color, move[0], move[1])
                score, bmove, bstart = alphaBetaMin(alpha, beta, chessBoard, color_op, depth - 1)
                alpha = max(score, alpha)
                if maxval <= score:
                    maxval = score
                    bestmove = move
                    beststart = (i // 8, i % 8)
                chessBoard.board[i // 8][i % 8] = figureMoved
                chessBoard.board[move[0]][move[1]] = figureCaptured
                if isinstance(figureMoved, King):
                    chessBoard.setKingPosition(figureMoved.color, i // 8, i % 8)
                # chessBoard.unmove(move[0], move[1], i // 8, i % 8, figureCaptured)
                if beta <= alpha:
                    break

    return maxval, bestmove, beststart


def alphaBetaMin(alpha, beta, chessBoard, color, depth):
    if depth == 0 or not chessBoard.can_move("w") or not chessBoard.can_move('b'):
        e = evaluate(chessBoard.board, color)
        return e, (0, 0), (0, 0)
    bestmove = None
    minval = 10**6
    beststart = (-1, -1)
    if color == 'w':
        color_op = 'b'
    else:
        color_op = 'w'
    for i in range(64):
        # print(alpha, beta)
        if chessBoard.board[i//8][i%8].color != color:
            pass
        else:
            for move in chessBoard.list_possible_moves(i//8, i % 8):
                # chessBoard.move(i//8, i % 8, move[0], move[1])
                figureCaptured = chessBoard.board[move[0]][move[1]]
                figureMoved = chessBoard.board[i // 8][i % 8]
                figureCaptured = chessBoard.board[move[0]][move[1]]
                chessBoard.board[i // 8][i % 8] = Empty()
                chessBoard.board[move[0]][move[1]] = figureMoved
                if isinstance(figureMoved, King):
                    chessBoard.setKingPosition(figureMoved.color, move[0], move[1])
                score, bmove, bstart = alphaBetaMax(alpha, beta, chessBoard, color_op, depth - 1)
                beta = min(score, beta)
                if score <= minval:
                    minval = score
                    bestmove = move
                    beststart = (i // 8, i % 8)
                # chessBoard.unmove(move[0], move[1], i//8, i % 8, figureCaptured)
                if isinstance(figureMoved, King):
                    chessBoard.setKingPosition(figureMoved.color, i//8, i % 8)
                chessBoard.board[i // 8][i % 8] = figureMoved
                chessBoard.board[move[0]][move[1]] = figureCaptured

                if beta <= alpha:
                    break
    return minval, bestmove, beststart

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
#
#     s, m, st = alphaBetaMax(-100000, 100000, chessBoard, 'w', 4)
#     print(s)
#     print(st)
#     print(m)
#


