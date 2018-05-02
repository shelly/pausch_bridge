import socketio
import eventlet
import events 

sio = socketio.Server()

@sio.on('connect')
def connect(sio, env):
	print("Connected")

@sio.on('message')
def message(sid, data):
	print("Received message", data) 


if __name__ == '__main__':
    app = socketio.Middleware(sio, app)
    eventlet.wsgi.server(eventlet.listen(('', 8000)), app)