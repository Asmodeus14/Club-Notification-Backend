import os
from flask import Flask
from flask_socketio import SocketIO
from dotenv import load_dotenv

load_dotenv(r"API.env")
# Load environment variables

REDIS_URL = os.getenv("REDIS_URL")

# Your Flask app setup
app = Flask(__name__)

# Initialize SocketIO with the Redis URL
socketio = SocketIO(app, cors_allowed_origins="https://club-notification-system.vercel.app", message_queue=REDIS_URL)

if __name__ == '__main__':
    socketio.run(app)
