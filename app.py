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
    # print(request.json['board'])
    # print(request.json['intact'])
    # print(request.json['position'])
    # print(request.json['w_king'], request.json['b_king'])
    board = Board(inputboard, w_king, b_king, intact)
    return jsonify({"result": board.list_possible_moves(request.json['position']['x'], request.json['position']['y'])})


@app.route("/changePosition", methods=['POST'])
def change():
    inputboard = request.json['board']
    w_king = request.json['w_king']
    b_king = request.json['b_king']
    initial = request.json['initial']
    final = request.json['final']
    intact = request.json['intact']
    print(request.json['intact'])
    board = Board(inputboard, w_king, b_king, intact)
    color = board.board[initial["x"]][initial["y"]].color
    board.move(initial["x"], initial["y"], final["x"], final["y"])
    if color == 'w':
        score, bestmove, startmove = alphaBetaMin(-1000, 1000, board, "b", 4)
    else:
        score, bestmove, startmove = alphaBetaMax(-1000, 1000, board, "w", 4)
    board.move(startmove[0], startmove[1], bestmove[0], bestmove[1])
    boardEncoder = BoardEncoder()
    res = BoardEncoder.encode(boardEncoder, board)

    return jsonify({"result": res})


@app.route("/static/<path:filename>")
def getJavaScript(filename):
    return send_from_directory(app.config['ES6_MODULES'], filename, as_attachment=True, mimetype='text/javascript')


if __name__ == '__main__':
    app.run()
