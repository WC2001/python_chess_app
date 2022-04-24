def valid_field(i, j):
    if i < 0 or i > 7 or j < 0 or j > 7:
        return False
    return True


class Piece:
    def __init__(self, color, piece):
        self.color = color
        self.piece = piece

    def list_possible_moves(self, x, y, board):
        return []


class Empty(Piece):
    def __init__(self):
        super().__init__('', '')

    def list_possible_moves(self, x, y, board):
        return []


class Rook(Piece):
    def __init__(self, color):
        super().__init__(color, 'R')

    def list_possible_moves(self, x, y, board):
        res = []
        for i in range(x + 1, 8):
            if board[i][y].color != self.color:
                res.append((i, y))
            if not isinstance(board[i][y], Empty):
                break
        for i in range(x - 1, -1, -1):
            if board[i][y].color != self.color:
                res.append((i, y))
            if not isinstance(board[i][y], Empty):
                break
        for i in range(y + 1, 8):
            if board[x][i].color != self.color:
                res.append((x, i))
            if not isinstance(board[x][i], Empty):
                break
        for i in range(y - 1, -1, -1):
            if board[x][i].color != self.color:
                res.append((x, i))
            if not isinstance(board[x][i], Empty):
                break
        return res


class Knight(Piece):
    def __init__(self, color):
        super().__init__(color, 'k')

    def list_possible_moves(self, x, y, board):
        res = []
        if valid_field(x - 1, y - 2) and board[x - 1][y - 2].color != self.color:
            res.append((x - 1, y - 2))
        if valid_field(x - 2, y - 1) and board[x - 2][y - 1].color != self.color:
            res.append((x - 2, y - 1))
        if valid_field(x - 2, y + 1) and board[x - 2][y + 1].color != self.color:
            res.append((x - 2, y + 1))
        if valid_field(x - 1, y + 2) and board[x - 1][y + 2].color != self.color:
            res.append((x - 1, y + 2))
        if valid_field(x + 1, y + 2) and board[x + 1][y + 2].color != self.color:
            res.append((x + 1, y + 2))
        if valid_field(x + 2, y + 1) and board[x + 2][y + 1].color != self.color:
            res.append((x + 2, y + 1))
        if valid_field(x + 2, y - 1) and board[x + 2][y - 1].color != self.color:
            res.append((x + 2, y - 1))
        if valid_field(x + 1, y - 2) and board[x + 1][y - 2].color != self.color:
            res.append((x + 1, y - 2))
        return res


class Bishop(Piece):
    def __init__(self, color):
        super().__init__(color, 'B')

    def list_possible_moves(self, x, y, board):
        res = []
        i = 1
        while valid_field(x + i, y + i):
            if board[x + i][y + i].color != self.color:
                res.append((x + i, y + i))
            if board[x + i][y + i].color != '':
                break
            i += 1
        i = 1
        while valid_field(x - i, y - i):
            if board[x - i][y - i].color != self.color:
                res.append((x - i, y - i))
            if not isinstance(board[x - i][y - i], Empty):
                break
            i += 1
        i = 1
        while valid_field(x + i, y - i):
            if board[x + i][y - i].color != self.color:
                res.append((x + i, y - i))
            if not isinstance(board[x + i][y - i], Empty):
                break
            i += 1
        i = 1
        while valid_field(x - i, y + i):
            if board[x - i][y + i].color != self.color:
                res.append((x - i, y + i))
            if not isinstance(board[x - i][y + i], Empty):
                break
            i += 1

        return res


class Pawn(Piece):
    def __init__(self, color):
        super().__init__(color, 'P')
        if self.color == 'b':
            self.step = 1
            self.start = 1
        elif self.color == 'w':
            self.step = -1
            self.start = 6

    def list_possible_moves(self, x, y, board):
        # TODO bicie w przelocie
        res = []
        if valid_field(x + self.step, y) and isinstance(board[x + self.step][y], Empty):
            res.append((x + self.step, y))
        if valid_field(x + self.step, y - 1) and not isinstance(board[x + self.step][y - 1], Empty) and \
                board[x + self.step][y - 1].color != self.color:
            res.append((x + self.step, y - 1))
        if valid_field(x + self.step, y + 1) and not isinstance(board[x + self.step][y + 1], Empty) and \
                board[x + self.step][y + 1].color != self.color:
            res.append((x + self.step, y + 1))
        if x == self.start and isinstance(board[x + self.step][y], Empty) and \
            isinstance(board[x + 2 * self.step][y], Empty):
            res.append((x + 2 * self.step, y))
        #Bicie w przelocie (chyba)
        # if valid_field(x + self.step, y + 1) and isinstance(self.board[x + self.step][y], Empty) and \
        #         isinstance(self.board[x][y + 1], Pawn) and self.color != self.board[x][y + 1].color:
        #     res.append((x + self.step, y + 1))
        # if valid_field(x + self.step, y - 1) and isinstance(self.board[x + self.step][y], Empty) and \
        #         isinstance(self.board[x][y - 1], Pawn) and self.board[x][y - 1].color != self.color:
        #     res.append((x + self.step, y - 1))
        return res


class Queen(Bishop, Rook):
    def __init__(self, color):
        Piece.__init__(self, color, 'Q')

    def list_possible_moves(self, x, y, board):
        return Bishop.list_possible_moves(self, x, y, board) + Rook.list_possible_moves(self, x, y, board)


class King(Piece):
    def __init__(self, color):
        super().__init__(color, 'K')

    def list_possible_moves(self, x, y, board):
        res = []
        if valid_field(x + 1, y) and board[x + 1][y].color != self.color:
            res.append((x + 1, y))
        if valid_field(x - 1, y) and board[x - 1][y].color != self.color:
            res.append((x - 1, y))
        if valid_field(x + 1, y + 1) and board[x + 1][y + 1].color != self.color:
            res.append((x + 1, y + 1))
        if valid_field(x + 1, y - 1) and board[x + 1][y - 1].color != self.color:
            res.append((x + 1, y - 1))
        if valid_field(x - 1, y - 1) and board[x - 1][y - 1].color != self.color:
            res.append((x - 1, y - 1))
        if valid_field(x - 1, y + 1) and board[x - 1][y + 1].color != self.color:
            res.append((x - 1, y + 1))
        if valid_field(x, y - 1) and board[x][y - 1].color != self.color:
            res.append((x, y - 1))
        if valid_field(x, y + 1) and board[x][y + 1].color != self.color:
            res.append((x, y + 1))
        #CASTLE
        if (self.color == 'b' and (x, y) == (0, 4)) or (self.color == 'w' and (x, y) == (7, 4)):
            if isinstance(board[x][y + 1], Empty) and isinstance(board[x][y + 2], Empty) and \
                    isinstance(board[x][y + 3], Rook):
                res.append((x, y + 3))

        return res

