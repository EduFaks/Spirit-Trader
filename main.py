import asyncio
from flask_socketio import SocketIO
from flask import Flask, render_template
from utils.stockEngine import price_listener

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('graph.html')


def send_prices(prices):
    socketio.emit('newdata', prices[-1])


def start_listener():
    asyncio.run(price_listener(send_prices))


if __name__ == '__main__':
    socketio.start_background_task(start_listener)
    socketio.run(app, allow_unsafe_werkzeug=True)
