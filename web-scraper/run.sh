#!/bin/bash

python backend/app.py &
FLASK_PID=$!

streamlit run main.py

kill $FLASK_PID