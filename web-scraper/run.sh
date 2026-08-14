#!/bin/bash

cd "$(dirname "$0")"

source .venv/bin/activate

python backend/app.py &
FLASK_PID=$!

streamlit run main.py

kill $FLASK_PID