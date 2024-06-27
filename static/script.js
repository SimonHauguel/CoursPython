const COLOR = {
    UNDEFINED : -1,
    BLACK : 0,
    WHITE : 1
};

let boardDOMElement = document.getElementById('board');
let board = new Array(8).fill(new Array(8).fill({color:COLOR.UNDEFINED, pawn:COLOR.UNDEFINED}));

let socket = io();

socket.on('connect', () => console.log('Connected to server'));
socket.on('message', msg => console.log('Received message:', msg));
socket.on("join_response", buildBoard )

socket.on('response_find_possible_move', val => console.log(val))

socket.emit("join", {"username" : "simon"});

function buildBoard(new_board) {

    if (new_board === undefined) {
        boardDOMElement.outerHTML = `<div id="error_message">Cannot join, 2 players are already playing</div>`;
        return
    }

    board = new_board;
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

            if (value.pawn == COLOR.WHITE) 
                acc += `<div class="pawn bg-white" onclick="socket.emit('find_possible_move', {x:${j}, y:${i}})"></div>`;
            
            else if (value.pawn == COLOR.BLACK) 
                acc += `<div class="pawn bg-black" onclick="socket.emit('find_possible_move', {x:${j}, y:${i}})"></div>`;

            acc += "</th>";
            
            j++;
        }
    
        i++;
        acc += "</tr>";
    }

    boardDOMElement.innerHTML = acc;

}