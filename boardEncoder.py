import json

from fieldEncoder import FieldEncoder
from boardIntactEncoder import BoardIntactEncoder
from board import Board


class BoardEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Board):
            res = {
                'board': [
                    [FieldEncoder().encode(obj.board[i][j]) for j in range(8)] for i in range(8)
                ],
                'intact': BoardIntactEncoder().encode(obj),
                'en_passant': [obj.return_en_passant[0], obj.return_en_passant[1]]

            }
            return res

        return json.JSONEncoder.default(self, obj)

