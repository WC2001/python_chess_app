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
    # print(request.json['board'])
    # print(request.json['intact'])
    # print(request.json['position'])
    # print(request.json['w_king'], request.json['b_king'])
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
    board.move(initial["x"], initial["y"], final["x"], final["y"])
    print('w', board.w_king_pos)
    print('b', board.b_king_pos)
    print('-----------')
    # print(evaluate(board.board, color))
    if board.mated():
        print('111')
        boardEncoder = BoardEncoder()
        res = BoardEncoder.encode(boardEncoder, board)
        return jsonify({"result": res})

    if color == 'w':
        score, bestmove, startmove = alphaBetaMin(-1000, 1000, board, "b", 3, color)
    else:
        score, bestmove, startmove = alphaBetaMax(-1000, 1000, board, "w", 3, color)
    board.move(startmove[0], startmove[1], bestmove[0], bestmove[1])

    # print(evaluate(board.board, color))
    print('w', board.w_king_pos)
    print('b', board.b_king_pos)
    print('-----------')
    boardEncoder = BoardEncoder()
    res = BoardEncoder.encode(boardEncoder, board)
    return jsonify({"result": res})


@app.route("/static/<path:filename>")
def getJavaScript(filename):
    return send_from_directory(app.config['ES6_MODULES'], filename, as_attachment=True, mimetype='text/javascript')


if __name__ == '__main__':
    app.run()
