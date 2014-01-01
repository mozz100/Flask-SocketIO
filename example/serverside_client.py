import logging

#logging.basicConfig(level=logging.DEBUG)

from socketIO_client import SocketIO, BaseNamespace

class TestNamespace(BaseNamespace):

    def on_my_response(self, *args):
        print 'on_my_response', args

socketIO = SocketIO('localhost', 5000)
test_namespace = socketIO.define(TestNamespace, '/test')

count = 0

while True:
    count += 1
    test_namespace.emit('my broadcast event', {'data': 'server event', 'count': count})
    socketIO.wait(seconds=10)

