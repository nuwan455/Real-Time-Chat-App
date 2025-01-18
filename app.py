from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)


@app.route('/')
def index():
    return render_template('index.html')


# When a message is sent
@socketio.on('message')
def handle_message(data):
    username = data.get('username')
    message = data.get('message')
    if username and message:
        print(f"Message from {username}: {message}")
        emit('message', {'username': username, 'message': message}, broadcast=True)


if __name__ == '__main__':
    socketio.run(app, debug=True)
