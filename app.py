from flask import Flask, render_template, request, jsonify, send_from_directory
from boardEncoder import BoardEncoder
from board import Board

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
    # print(request.json['board'])
    # print(request.json['position'])
    # print(request.json['w_king'], request.json['b_king'])
    board = Board(inputboard, w_king, b_king)
    return jsonify({"result": board.list_possible_moves(request.json['position']['x'], request.json['position']['y'])})


@app.route("/changePosition", methods=['POST'])
def change():
    inputboard = request.json['board']
    w_king = request.json['w_king']
    b_king = request.json['b_king']
    initial = request.json['initial']
    final = request.json['final']
    board = Board(inputboard, w_king, b_king)
    board.move(initial["x"], initial["y"], final["x"], final["y"])
    boardEncoder = BoardEncoder()
    res = BoardEncoder.encode(boardEncoder, board)

    return jsonify({"result": res})




@app.route("/static/<path:filename>")
def getJavaScript(filename):
    return send_from_directory(app.config['ES6_MODULES'], filename, as_attachment=True, mimetype='text/javascript')


if __name__ == '__main__':
    app.run()
