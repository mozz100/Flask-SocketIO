#!/bin/bash
gunicorn -b 0.0.0.0:5000 --worker-class socketio.sgunicorn.GeventSocketIOWorker app:app
