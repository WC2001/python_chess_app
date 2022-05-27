from random import randint

from figures import Piece, Rook, Knight, Bishop, Pawn, Empty, Queen, King


def valid_field(i, j):
    if i < 0 or i > 7 or j < 0 or j > 7:
        return False
    return True


class Board:

    def __init__(self, board, w_king, b_king, intact, player, en_passant):
        B = [[] for _ in range(8)]
        for i in range(64):
            if board[i // 8][i % 8]["piece"] == "K":
                if board[i // 8][i % 8]["color"] == "w":
                    B[i // 8].append(King("w"))
                else:
                    B[i // 8].append(King("b"))

            if board[i // 8][i % 8]["piece"] == "Q":
                if board[i // 8][i % 8]["color"] == "w":
                    B[i // 8].append(Queen("w"))
                else:
                    B[i // 8].append(Queen("b"))

            if board[i // 8][i % 8]["piece"] == "B":
                if board[i // 8][i % 8]["color"] == "w":
                    B[i // 8].append(Bishop("w"))
                else:
                    B[i // 8].append(Bishop("b"))

            if board[i // 8][i % 8]["piece"] == "k":
                if board[i // 8][i % 8]["color"] == "w":
                    B[i // 8].append(Knight("w"))
                else:
                    B[i // 8].append(Knight("b"))

            if board[i // 8][i % 8]["piece"] == "R":
                if board[i // 8][i % 8]["color"] == "w":
                    B[i // 8].append(Rook("w"))
                else:
                    B[i // 8].append(Rook("b"))

            if board[i // 8][i % 8]["piece"] == "P":
                if board[i // 8][i % 8]["color"] == "w":
                    B[i // 8].append(Pawn("w", player))
                else:
                    B[i // 8].append(Pawn("b", player))

            if board[i // 8][i % 8]["piece"] == "":
                B[i // 8].append(Empty())

        self.board = B
        self.w_king_pos = (w_king["x"], w_king["y"])
        self.b_king_pos = (b_king["x"], b_king["y"])
        self.w_short = intact["w_short"]
        self.w_long = intact["w_long"]
        self.b_short = intact["b_short"]
        self.b_long = intact["b_long"]
        self.w_king_intact = intact["w_king"]
        self.b_king_intact = intact["b_king"]
        self.player = player
        self.en_passant = [-1, -1]
        self.return_en_passant = en_passant
        self.w_king_mated = 0
        self.b_king_mated = 0

    def in_check(self, x, y):
        color = self.board[x][y].color
        i = 1
        while valid_field(x, y + i):
            if self.board[x][y + i].color == color:
                break
            if self.board[x][y + i].color != color and self.board[x][y + i].color != '' and \
                    (self.board[x][y + i].piece != 'Q' and self.board[x][y + i].piece != 'R'):
                break
            if self.board[x][y + i].color != color and self.board[x][y + i].color != '' and \
                    (self.board[x][y + i].piece == 'Q' or self.board[x][y + i].piece == 'R'):
                print(x, y)
                return True
            i += 1
        i = 1
        while valid_field(x, y - i):
            if self.board[x][y - i].color == color:
                break
            if self.board[x][y - i].color != color and self.board[x][y - i].color != '' and \
                    (self.board[x][y - i].piece != 'Q' and self.board[x][y - i].piece != 'R'):
                break
            if self.board[x][y - i].color != color and self.board[x][y - i].color != '' and \
                    (self.board[x][y - i].piece == 'Q' or self.board[x][y - i].piece == 'R'):
                return True
            i += 1

        i = 1
        while valid_field(x - i, y):
            if self.board[x - i][y].color == color:
                break
            if self.board[x - i][y].color != color and self.board[x - i][y].color != '' and \
                    (self.board[x - i][y].piece != 'Q' and self.board[x - i][y].piece != 'R'):
                break
            if self.board[x - i][y].color != color and self.board[x - i][y].color != '' and \
                    (self.board[x - i][y].piece == 'Q' or self.board[x - i][y].piece == 'R'):
                return True
            i += 1

        i = 1
        while valid_field(x + i, y):
            if self.board[x + i][y].color == color:
                break
            if self.board[x + i][y].color != color and self.board[x + i][y].color != '' and \
                    (self.board[x + i][y].piece != 'Q' and self.board[x + i][y].piece != 'R'):
                break
            if self.board[x + i][y].color != color and self.board[x + i][y].color != '' and \
                    (self.board[x + i][y].piece == 'Q' or self.board[x + i][y].piece == 'R'):
                return True
            i += 1

        i = 1
        while valid_field(x - i, y - i):
            if self.board[x - i][y - i].color == color:
                break
            if self.board[x - i][y - i].color != color and self.board[x - i][y - i].color != '' and \
                    (self.board[x - i][y - i].piece != 'Q' and self.board[x - i][y - i].piece != 'B'):
                break
            if self.board[x - i][y - i].color != color and self.board[x - i][y - i].color != '' and \
                    (self.board[x - i][y - i].piece == 'Q' or self.board[x - i][y - i].piece == 'B'):
                return True
            i += 1
        i = 1
        while valid_field(x + i, y + i):
            if self.board[x + i][y + i].color == color:
                break
            if self.board[x + i][y + i].color != color and self.board[x + i][y + i].color != '' and \
                    (self.board[x + i][y + i].piece != 'Q' and self.board[x + i][y + i].piece != 'B'):
                break
            if self.board[x + i][y + i].color != color and self.board[x + i][y + i].color != '' and \
                    (self.board[x + i][y + i].piece == 'Q' or self.board[x + i][y + i].piece == 'B'):
                return True
            i += 1
        i = 1
        while valid_field(x + i, y - i):
            if self.board[x + i][y - i].color == color:
                break
            if self.board[x + i][y - i].color != color and self.board[x + i][y - i].color != '' and \
                    (self.board[x + i][y - i].piece != 'Q' and self.board[x + i][y - i].piece != 'B'):
                break
            if self.board[x + i][y - i].color != color and self.board[x + i][y - i].color != '' and \
                    (self.board[x + i][y - i].piece == 'Q' or self.board[x + i][y - i].piece == 'B'):
                return True
            i += 1
        i = 1
        while valid_field(x - i, y + i):
            if self.board[x - i][y + i].color == color:
                break
            if self.board[x - i][y + i].color != color and self.board[x - i][y + i].color != '' and \
                    (self.board[x - i][y + i].piece != 'Q' and self.board[x - i][y + i].piece != 'B'):
                break
            if self.board[x - i][y + i].color != color and self.board[x - i][y + i].color != '' and \
                    (self.board[x - i][y + i].piece == 'Q' or self.board[x - i][y + i].piece == 'B'):
                return True
            i += 1

        if valid_field(x - 1, y - 2) and self.board[x - 1][y - 2].color != color and self.board[x - 1][y - 2].piece == 'k':
            return True
        if valid_field(x - 2, y - 1) and self.board[x - 2][y - 1].color != color and self.board[x - 2][y - 1].piece == 'k':
            return True
        if valid_field(x - 2, y + 1) and self.board[x - 2][y + 1].color != color and self.board[x - 2][y + 1].piece == 'k':
            return True
        if valid_field(x - 1, y + 2) and self.board[x - 1][y + 2].color != color and self.board[x - 1][y + 2].piece == 'k':
            return True
        if valid_field(x + 1, y + 2) and self.board[x + 1][y + 2].color != color and self.board[x + 1][y + 2].piece == 'k':
            return True
        if valid_field(x + 2, y + 1) and self.board[x + 2][y + 1].color != color and self.board[x + 2][y + 1].piece == 'k':
            return True
        if valid_field(x + 2, y - 1) and self.board[x + 2][y - 1].color != color and self.board[x + 2][y - 1].piece == 'k':
            return True
        if valid_field(x + 1, y - 2) and self.board[x + 1][y - 2].color != color and self.board[x + 1][y - 2].piece == 'k':
            return True
        if color == 'w':
            i = -1 if self.player == 'w' else 1
            if valid_field(x + i, y - 1) and self.board[x + i][y - 1].color == 'b' and self.board[x + i][y - 1].piece == 'P':
                return True
            if valid_field(x + i, y + 1) and self.board[x + i][y + 1].color == 'b' and self.board[x + i][y + 1].piece == 'P':
                return True

        if color == 'b':
            i = 1 if self.player == 'w' else -1
            if valid_field(x + i, y - 1) and self.board[x + i][y - 1].color == 'w' and self.board[x + i][y - 1].piece == 'P':
                return True
            if valid_field(x + i, y + 1) and self.board[x + i][y + 1].color == 'w' and self.board[x + i][y + 1].piece == 'P':
                return True

        if color == 'w' and abs(self.b_king_pos[0] - x) <= 1 and abs(self.b_king_pos[1] - y) <= 1:
            return True
        if color == 'b' and abs(self.w_king_pos[0] - x) <= 1 and abs(self.w_king_pos[1] - y) <= 1:
            return True

        return False

    def list_possible_moves(self, x, y):
        arr = list(filter(lambda m: self.test_move(m, x, y), self.board[x][y].list_possible_moves(x, y, self)))
        return arr

    def test_move(self, move, x, y):
        old = self.board[x][y]
        move_field = self.board[move[0]][move[1]]
        if self.board[x][y].piece == 'K' and self.board[x][y].color == 'w':
            self.w_king_pos = move
        if self.board[x][y].piece == 'K' and self.board[x][y].color == 'b':
            self.b_king_pos = move

        self.board[x][y] = Empty()

        self.board[move[0]][move[1]] = old

        if old.color == 'w' and self.in_check(self.w_king_pos[0], self.w_king_pos[1]):
            self.board[x][y] = old
            self.board[move[0]][move[1]] = move_field
            if old.piece == 'K':
                self.w_king_pos = (x, y)
            return False

        if old.color == 'b' and self.in_check(self.b_king_pos[0], self.b_king_pos[1]):
            self.board[x][y] = old
            self.board[move[0]][move[1]] = move_field
            if old.piece == 'K':
                self.b_king_pos = (x, y)
            return False

        if old.color == 'b' and old.piece == 'K':
            self.b_king_pos = (x, y)

        if old.color == 'w' and old.piece == 'K':
            self.w_king_pos = (x, y)

        self.board[x][y] = old
        self.board[move[0]][move[1]] = move_field
        return True

    def can_move(self, color):
        for i in range(8):
            for j in range(8):
                if self.board[i][j].color == color:
                    if len(self.list_possible_moves(i, j)) > 0:
                        print(self.board[i][j].piece, self.list_possible_moves(i, j))
                        return True

        return False

    def move(self, x, y, x1, y1):
        color = self.board[x][y].color
        playerTurn = color == self.player

        if isinstance(self.board[x][y], King):
            print('king')
            self.setKingPosition(color, x1, y1)
            self.updateCastle(x, y, y1)
        self.setEnPassant(playerTurn, -1, -1)
        if isinstance(self.board[x][y], Pawn):
            self.en_passantUpdate(color, x, y, x1)

        if isinstance(self.board[x][y], Rook) and self.player == 'w':
            if y == 0:
                self.changeIntact(color, long=True)
            if y == 7:
                self.changeIntact(color, short=True)

        if isinstance(self.board[x][y], Rook) and self.player == 'b':
            if y == 0:
                self.changeIntact(color, short=True)
            if y == 7:
                self.changeIntact(color, long=True)

        if self.player == self.board[x][y].color and self.board[x][y].piece == 'P' and \
                x1 == self.return_en_passant[0] and y1 == self.return_en_passant[1]:
            self.board[x][y1] = Empty()
        if self.player != self.board[x][y].color and self.board[x][y].piece == 'P' and \
                x1 == self.en_passant[0] and y1 == self.en_passant[1]:
            self.board[x][y1] = Empty()

        self.board[x1][y1] = self.board[x][y]
        self.board[x][y] = Empty()
        if isinstance(self.board[x1][y1], Pawn) and (x1 == 0 or x1 == 7):
            self.upgradePawn(x1, y1, color)
        if color == 'w' and self.in_check(self.b_king_pos[0], self.b_king_pos[1]):
            print("Black king checked.")
            if not self.can_move('b'):
                self.b_king_mated = 1
                print("Black king mated")
        if color == 'b' and self.in_check(self.w_king_pos[0], self.w_king_pos[1]):
            print("White king checked.")
            if not self.can_move('w'):
                self.w_king_mated = 1
                print("White king mated")

    def setKingPosition(self, color, x, y):
        if color == 'w':
            self.w_king_pos = (x, y)
        else:
            self.b_king_pos = (x, y)

    def en_passantUpdate(self, color, x, y, x1):
        playerTurn = color == self.player
        self.setEnPassant(playerTurn, -1, -1)
        if x == 6 and x1 == 4:
            self.setEnPassant(playerTurn, 5, y)
        elif x == 1 and x1 == 3:
            self.setEnPassant(playerTurn, 2, y)


    def setEnPassant(self, playerTurn, x, y):
        if playerTurn:
            self.en_passant[0] = x
            self.en_passant[1] = y
        else:
            self.return_en_passant[0] = x
            self.return_en_passant[1] = y

    def updateCastle(self, x, y, y1):
        color = self.board[x][y].color
        if self.player == 'w':
            if y1 == y + 2:
                self.move(x, y+3, x, y+1)
                self.changeIntact(color, king=True, short=True)
            if y1 == y - 2:
                self.move(x, y - 4, x, y - 1)
                self.changeIntact(color, king=True, long=True)
            else:
                self.changeIntact(color, king=True)
        else:
            if y1 == y - 2:
                self.move(x, y - 3, x, y - 1)
                self.changeIntact(color, king=True, short=True)
            if y1 == y + 2:
                self.move(x, y + 4, x, y + 1)
                self.changeIntact(color, king=True, long=True)
            else:
                self.changeIntact(color, king=True)

    def changeIntact(self, color, king=False, long=False, short=False):
        if color == 'w':
            if king:
                self.w_king_intact = 0
            if long:
                self.w_long = 0
            elif short:
                self.w_short = 0
        if color == 'b':
            if king:
                self.b_king_intact = 0
            if long:
                self.b_long = 0
            elif short:
                self.b_short = 0

    def mated(self):
        return self.w_king_mated or self.b_king_mated


    def upgradePawn(self, x, y, color):
        updates = [Knight, Queen, Rook, Bishop]
        self.board[x][y] = updates[randint(0, 4)](color)