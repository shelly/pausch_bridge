import socketio
import eventlet
import demo

sio = socketio.Server()

@sio.on('connection')
def connect(sio, env):
	pass 

@sio.on('message')
def message(sid, data):
	print("Text: ", data['text'], "Color: ", data['color'])
	updateText(data['text'], data['color'])
	sio.emit('reply', {data['text'], data['color']})


if __name__ == '__main__':
    app = socketio.Middleware(sio)
    eventlet.wsgi.server(eventlet.listen(('', 8000)), app)
