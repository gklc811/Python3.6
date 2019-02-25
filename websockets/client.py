from socketIO_client import SocketIO, LoggingNamespace


def on_aaa_response(args):
    print('on_aaa_response', args)


socketIO = SocketIO('localhost', 8080, LoggingNamespace)
socketIO.emit('GET_SAMPLE_REQUEST')
socketIO.on('GET_SAMPLE_RESPONSE', on_aaa_response)

socketIO.wait(seconds=1)
