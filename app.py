from flask import Flask, render_template
from flask_socketio import SocketIO, send, emit

app = Flask(__name__)
socketio = SocketIO(app)

# In-memory message storage (for simplicity)
messages = []

@app.route('/')
def index():
    return render_template('chat.html', messages=messages)

@socketio.on('message')
def handle_message(data):
    messages.append({'username': data['username'], 'message': data['message']})
    emit('message', data, broadcast=True)

if __name__ == '__main__':
    socketio.run(app,host="0.0.0.0", port=8000)
