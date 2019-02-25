from traceback import print_exc
from flask import Flask, request, session
from flask_socketio import SocketIO, emit
from pandas import read_sql_query, to_datetime
import json

app = Flask(__name__)
socketio = SocketIO(app, path='sample')


@socketio.on('GET_SAMPLE_REQUEST')
def handle_message():
    print("Server Hit ******************************************************")
    emit('GET_SAMPLE_RESPONSE', {'percentage': '100', 'message': 'Complete', 'status': True},
         json=True)


if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=8080, debug=True, use_reloader=False)
