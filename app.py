from flask import Flask, render_template, request, jsonify, send_from_directory

from board import Board
from boardEncoder import BoardEncoder
from evaluation import alphaBetaMax, alphaBetaMin, evaluate
app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return render_template("index.html")


@app.route("/moves", methods=['POST'])
def moves():
    x = request.args.get('x')
    y = request.args.get('y')
    inputboard = request.json['board']
    w_king = request.json['w_king']
    b_king = request.json['b_king']
    intact = request.json['intact']
    player = request.json['player']
    enpassant = request.json['en_passant']
    board = Board(inputboard, w_king, b_king, intact, player, enpassant)

    return jsonify({"result": board.list_possible_moves(request.json['position']['x'], request.json['position']['y'])})


@app.route("/changePosition", methods=['POST'])
def change():
    inputboard = request.json['board']
    w_king = request.json['w_king']
    b_king = request.json['b_king']
    initial = request.json['initial']
    final = request.json['final']
    intact = request.json['intact']
    player = request.json['player']
    enpassant = request.json['en_passant']

    board = Board(inputboard, w_king, b_king, intact, player, enpassant)
    color = board.board[initial["x"]][initial["y"]].color
    print(evaluate(board.board, color))
    description = board.get_move_description(initial["x"], initial["y"], final["x"], final["y"])
    description1 = ''
    board.move(initial["x"], initial["y"], final["x"], final["y"])

    # print('w', board.w_king_pos)
    # print('b', board.b_king_pos)
    # print('-----------')
    # print(evaluate(board.board, color))
    if board.mated() or board.draw:
        boardEncoder = BoardEncoder()
        res = BoardEncoder.encode(boardEncoder, board)
        return jsonify({"result": res, "move_description": [description, description1]})

    if color == 'w':
        score, bestmove, startmove = alphaBetaMin(-10000, 10000, board, "b", 3, color)
    else:
        score, bestmove, startmove = alphaBetaMax(-10000, 10000, board, "w", 3, color)
    description1 = board.get_move_description(startmove[0], startmove[1], bestmove[0], bestmove[1])
    board.move(startmove[0], startmove[1], bestmove[0], bestmove[1])

    # print('w', board.w_king_pos)
    # print('b', board.b_king_pos)
    # print('-----------')
    boardEncoder = BoardEncoder()
    res = BoardEncoder.encode(boardEncoder, board)
    return jsonify({"result": res, "move_description": [description, description1]})


@app.route("/firstMove", methods=['POST'])
def firstMove():
    inputboard = request.json['board']
    w_king = request.json['w_king']
    b_king = request.json['b_king']
    intact = request.json['intact']
    player = request.json['player']
    enpassant = request.json['en_passant']
    board = Board(inputboard, w_king, b_king, intact, player, enpassant)
    # print('w', board.w_king_pos)
    # print('b', board.b_king_pos)
    # print('-----------')

    description = ''
    description1 = ''

    if player == 'b':
        score, bestmove, startmove = alphaBetaMax(-10000, 10000, board, "w", 3, player)
        description = board.get_move_description(startmove[0], startmove[1], bestmove[0], bestmove[1])
        board.move(startmove[0], startmove[1], bestmove[0], bestmove[1])

    # print('w', board.w_king_pos)
    # print('b', board.b_king_pos)
    # print('-----------')
    boardEncoder = BoardEncoder()
    res = BoardEncoder.encode(boardEncoder, board)
    return jsonify({"result": res, "move_description": [description, description1]})


@app.route("/static/<path:filename>")
def getJavaScript(filename):
    return send_from_directory(app.config['ES6_MODULES'], filename, as_attachment=True, mimetype='text/javascript')


if __name__ == '__main__':
    app.run()
