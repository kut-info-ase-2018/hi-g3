const http = require('http');
const socketio = require('socket.io');
const fs = require('fs');

const index_page = fs.readFileSync(__dirname + '/index.html', 'utf-8');

var host = '192.168.33.10';
var port = 8000;

var count = 0;

server = http.createServer(createServ);

function createServ(req, res) {
    console.log("req.method " + req.method);
    res.writeHead(200, {'Content-Type' : 'text/html'});
    res.end(index_page);
}

server.listen(port);
console.log("Server Start!");

var io = socketio.listen(server);

setInterval(function() {
    console.log("count: " + count);
    count++;
}, 1000);

io.sockets.on('connection', function(socket) {
    console.log("Socket Connected!");
    setInterval(function() {
        socket.emit('count_data', {value : count});
    }, 1000);
});