#!/bin/bash
gunicorn -k eventlet -w 1 Auth:app --bind 0.0.0.0:$PORT
