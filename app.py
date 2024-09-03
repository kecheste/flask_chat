from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit
from abc import ABC, abstractmethod

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'
socketio = SocketIO(app)

class Observer(ABC):
    @abstractmethod
    def update(self, message: str, is_self: bool):
        pass

class Client(Observer):
    def __init__(self, session_id, username):
        self.session_id = session_id
        self.username = username

    def update(self, message: str, is_self: bool = False):
        if is_self:
            message = "You joined the chat."
        socketio.emit('message', {'msg': message}, room=self.session_id)

class ChatRoom:
    def __init__(self):
        self._clients = []

    def attach(self, client: Client):
        self._clients.append(client)
        self.notify(f"{client.username} has joined the chat.", client)
        self.update_user_list()

    def detach(self, client: Client):
        if client in self._clients:
            self.notify(f"{client.username} has left the chat.")
            self._clients.remove(client)
            self.update_user_list()

    def notify(self, message: str, new_client: Client = None):
        for client in self._clients:
            is_self = client == new_client
            client.update(message, is_self)

    def update_user_list(self):
        usernames = [client.username for client in self._clients]
        socketio.emit('update_users', {'users': usernames})

    def broadcast(self, message: str):
        self.notify(message)

chat_room = ChatRoom()

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('new_user')
def handle_new_user(data):
    username = data['username']
    client = Client(session_id=request.sid, username=username)
    chat_room.attach(client)
    print(f'Client {request.sid} connected as {username}.')

@socketio.on('disconnect')
def handle_disconnect():
    client = next((c for c in chat_room._clients if c.session_id == request.sid), None)
    if client:
        chat_room.detach(client)
    print(f'Client {request.sid} disconnected.')

@socketio.on('leave_chat')
def handle_leave_chat():
    client = next((c for c in chat_room._clients if c.session_id == request.sid), None)
    if client:
        chat_room.detach(client)
        emit('redirect', {'url': '/'}, room=request.sid)

@socketio.on('message')
def handle_message(msg):
    client = next((c for c in chat_room._clients if c.session_id == request.sid), None)
    if client:
        formatted_message = f"{client.username}: {msg}"
        chat_room.broadcast(formatted_message)

if __name__ == '__main__':
    socketio.run(app, debug=False)
