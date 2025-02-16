#!/bin/bash
gunicorn -k eventlet -w 1 auth:app --bind 0.0.0.0:$PORT
