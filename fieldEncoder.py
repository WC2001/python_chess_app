import json

from figures import Piece


class FieldEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Piece):
            res = {
                'piece': obj.piece,
                'color': obj.color
            }
            return res

        return json.JSONEncoder.default(self, obj)

