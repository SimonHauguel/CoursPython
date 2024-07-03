from flask import Flask, render_template
from flask_socketio import SocketIO, send, emit

from utils import *
from part1 import *
from part2 import *
from part3 import *

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
    emit("response_find_possible_move", find_all_possible_moves(board, (location["x"], location["y"])))

@socketio.on('move')
def handle_move(info_object):
    
    emit("response_move", move_pawn(board, (info_object["from"]["x"], info_object["from"]["y"]), (info_object["to"]["x"], info_object["to"]["y"])).data_board)



@socketio.on("join")
def handle_new_join(obj_username):

    username = obj_username["username"]
    res = build_initial_board(board)

    if (res): board.players.append(username)

    for x in res: 
        for y in x: y["available_move"] = False

    emit("join_response", res)

socketio.run(app, debug=True)