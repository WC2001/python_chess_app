from figures import Empty


def evaluate(board, color):
    value = 0

    for i in range(64):
        row = i//8 if color == 'w' else 7 - i//8
        colorFactor = 1 if board[i//8][i % 8].color == 'w' else -1
        value += colorFactor * board[i//8][i % 8].value + board[i//8][i % 8].valueAdjustment[row][i % 8]

    return value


def alphaBetaMax(alpha, beta, chessBoard, color, depth):
    if depth == 0:
        return evaluate(chessBoard.board, color)
    bestmove = None
    for i in range(64):
        for move in chessBoard.list_possible_moves(i//8, i % 8):
            figureCaptured = chessBoard.board[move[0]][move[1]]
            figureMoved = chessBoard.board[i//8][i % 8]
            chessBoard.board[i // 8][i % 8] = Empty()
            chessBoard.board[move[0]][move[1]] = figureMoved

            if color == 'w':
                color = 'b'
            else:
                color = 'w'
            score = alphaBetaMin(alpha, beta, chessBoard, color, depth - 1)

            chessBoard.board[i // 8][i % 8] = figureMoved
            chessBoard.board[move[0]][move[1]] = figureCaptured

            if score >= beta:
                return beta, move
            if alpha >= score:
                alpha = score
                bestmove = move

            # alpha = max(alpha, score)

    return alpha, bestmove


def alphaBetaMin(alpha, beta, chessBoard, color, depth):
    if depth == 0:
        return evaluate(chessBoard, color)

    for i in range(64):
        for move in chessBoard.list_possible_moves(i // 8, i % 8):
            figureCaptured = chessBoard.board[move[0]][move[1]]
            figureMoved = chessBoard.board[i // 8][i % 8]
            chessBoard.board[i // 8][i % 8] = Empty()
            chessBoard.board[move[0]][move[1]] = figureMoved

            if color == 'w':
                color = 'b'
            else:
                color = 'w'
            score = alphaBetaMin(alpha, beta, chessBoard, color, depth - 1)

            chessBoard.board[i // 8][i % 8] = figureMoved
            chessBoard.board[move[0]][move[1]] = figureCaptured
            if score <= alpha:
                return alpha

            beta = min(beta, score)

    return beta



