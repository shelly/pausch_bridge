var app = require('express')();
var http = require('http').Server(app);
var io = require('socket.io')(http);

app.get('/', function(req, res){
  res.sendFile(__dirname + '/index.html');
});

io.on('connection', function(socket){
  socket.on('message', function(text, color){
  	io.emit('message', text, color);
  });
});

http.listen(3000, function(){
  console.log('listening on *:3000');
});
    