from board import Board
import json


class BoardIntactEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Board):
            res = {
                'w_short': obj.w_short,
                'w_long': obj.w_long,
                'w_king_intact': obj.w_king_intact,
                'b_short': obj.b_short,
                'b_long': obj.b_long,
                'b_king_intact': obj.b_king_intact

            }
            return res

        return json.JSONEncoder.default(self, obj)

