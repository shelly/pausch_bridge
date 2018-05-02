import socketio
import eventlet
import demo

sio = socketio.Server()

@sio.on('connection')
def connect(sio, env):
	print("Connected")

@sio.on('message')
def message(sid, data):
	print("Received message", data) 
	updateText(data['text'], data['color'])


if __name__ == '__main__':
    app = socketio.Middleware(sio)
    eventlet.wsgi.server(eventlet.listen(('', 8000)), app)
