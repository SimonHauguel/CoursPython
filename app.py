from flask import Flask, render_template
from flask_socketio import SocketIO, send, emit

from utils import *
from part1 import *

board = Board()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('message')
def handle_message(msg):
    print(f'Received message: {msg}')
    send(f'Echo: {msg}')

@socketio.on('find_possible_move')
def handle_find_possible_move(location):
    
    solutions_data = {"solutions" : []}

    if (0 > location["x"] or location["x"] > 7 or 0 > location["y"] or location["y"] > 7): 
        emit("response_find_possible_move", solutions_data)

    solutions = solutions_data["solutions"]

    loc_x = location["x"]
    loc_y = location["y"]

    if board.actual_player == TILE.WHITE:

        if (1 <= loc_x <= 6 and 1 <= loc_y <= 6):
            if board.get_value_at(loc_x-1, loc_y-1) == PAWN.NO_PAWN:
                solutions.append({"x" : loc_x-1, "y" : loc_y-1})
            if board.get_value_at(loc_x+1, loc_y-1) == PAWN.NO_PAWN:
                solutions.append({"x" : loc_x+1, "y" : loc_y-1})

    elif board.actual_player == TILE.BLACK:
        if (1 <= loc_x <= 6 and 1 <= loc_y <= 6):
            if board.get_value_at(loc_x-1, loc_y-1) == PAWN.NO_PAWN:
                solutions.append({"x":loc_x-1, "y":loc_y-1})
            if board.get_value_at(loc_x+1, loc_y-1) == PAWN.NO_PAWN:
                solutions.append({"x":loc_x+1, "y":loc_y-1})


    emit("response_find_possible_move", solutions_data)


@socketio.on("join")
def handle_new_join(obj_username):

    username = obj_username["username"]
    res = build_initial_board(board)

    if (res): board.players.append(username)

    emit("join_response", res)

socketio.run(app, debug=True)