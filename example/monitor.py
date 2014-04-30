from socketIO_client import SocketIO, BaseNamespace
from gevent.socket import wait_read, timeout
import sys
import gevent
from gevent import monkey
import psutil

monkey.patch_all()

class TestNamespace(BaseNamespace):
    def on_my_response(self, *args):
        print args

socketIO = SocketIO('localhost', 5000)
test_namespace = socketIO.define(TestNamespace, '/ps')

def ticker():
    count = 0
    while True:
        count += 1
        test_namespace.emit('data', {'processor': psutil.cpu_percent(), 'count': count})
        gevent.sleep(2)

greenlets = [gevent.Greenlet.spawn(f) for f in (
    # socketIO.wait, # for receiving events from browsers
    ticker,
)]

gevent.joinall(greenlets)
