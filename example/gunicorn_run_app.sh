#!/bin/bash
gunicorn --workers 1 -b 0.0.0.0:5000 --worker-class socketio.sgunicorn.GeventSocketIOWorker app:app
