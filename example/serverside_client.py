from socketIO_client import SocketIO, BaseNamespace
from gevent.socket import wait_read, timeout
import sys
import gevent
from gevent import monkey

monkey.patch_socket() # othersie socketIO.wait seems to block

class TestNamespace(BaseNamespace):
    def on_my_response(self, *args):
        print args

socketIO = SocketIO('localhost', 5000)
test_namespace = socketIO.define(TestNamespace, '/test')

def stdin_reader():
    count = 0
    while True:
        count += 1
        try:
            wait_read(sys.stdin.fileno(), timeout=3)
            line = sys.stdin.readline().strip()
            test_namespace.emit('my broadcast event', {'data': line, 'count': count})
        except timeout:
            test_namespace.emit('my broadcast event', {'data': 'tick', 'count': count})

greenlets = [gevent.Greenlet.spawn(f) for f in (socketIO.wait, stdin_reader)]

gevent.joinall(greenlets)
