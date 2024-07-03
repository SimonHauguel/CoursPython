const COLOR = {
    UNDEFINED : -1,
    BLACK : 0,
    WHITE : 1
};

let boardDOMElement = document.getElementById('board');
let board = new Array(8).fill(new Array(8).fill({color:COLOR.UNDEFINED, pawn:COLOR.UNDEFINED, available_move:false}));

let socket = io();

let actual_selectioned_pawn = undefined;

socket.on('connect', () => console.log('Connected to server'));
socket.on('message', msg => console.log('Received message:', msg));
socket.on("join_response", buildBoardAndSet )

socket.on('response_find_possible_move',

    answer => {

        console.log("-- response_find_possible_move's answer :", answer)

        for (let i = 0; i <= 7; i++)
            for (let j = 0; j <= 7; j++)
                board[j][i].available_move = false

        for ([x, y] of answer) board[y][x].available_move = true

        console.log("-- response_find_possible_move's new board :", board)

        buildBoard(board)
    }
)

socket.on("response_move", x => buildBoardAndSet(x))

socket.emit("join", {"username" : "simon"});

function buildBoardAndSet(new_board) {
    board = new_board;
    buildBoard(new_board)
}

function buildBoard(new_board) {

    if (new_board === undefined) {
        boardDOMElement.outerHTML = `<div id="error_message">Cannot join, 2 players are already playing</div>`;
        return
    }
    acc = "";

    let i = 0;
    let j = 0;

    for (let line of board) {
    
        j = 0;
        acc += "<tr>";

        for (let value of line) {
            if (value.tile == COLOR.WHITE)      acc += `<th class="tile bg-white">`;
            else if (value.tile == COLOR.BLACK) acc += `<th class="tile bg-black">`;
            else acc += `<th class="bg_undefined tile">`;

            if (value.available_move) 
                acc += `<div class="available-move" onclick="socket.emit('move', {from: actual_selectioned_pawn, to:{x:${j}, y:${i}}})"></div>`;

            else if (value.pawn == COLOR.WHITE) 
                acc += `<div class="pawn bg-white" onclick="socket.emit('find_possible_move', {x:${j}, y:${i}}); actual_selectioned_pawn={x:${j}, y:${i}}; console.log(actual_selectioned_pawn)"></div>`;
            
            else if (value.pawn == COLOR.BLACK) 
                acc += `<div class="pawn bg-black" onclick="socket.emit('find_possible_move', {x:${j}, y:${i}}); actual_selectioned_pawn={x:${j}, y:${i}}; console.log(actual_selectioned_pawn)"></div>`;

            acc += "</th>";
            
            j++;
        }
    
        i++;
        acc += "</tr>";
    }

    boardDOMElement.innerHTML = acc;

}