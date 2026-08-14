from flask import Flask, jsonify
import newsapi
import requests
import os
import json
import streamlit as st

app = Flask(__name__)

api_key = st.secrets["NEWSAPI_KEY"]

client = newsapi.NewsApiClient(
    api_key=api_key
)


@app.route("/sources")
def get_sources():
    response = requests.get(
        f"https://newsapi.org/v2/top-headlines/sources?apiKey={api_key}"
    )
    response.raise_for_status()

    data = response.json()

    with open("sources.json", "w") as f:
        json.dump(data, f, indent=4)

    return jsonify(data)


@app.route("/headlines")
def get_headlines():
    data = client.get_top_headlines(
        q="AI OR Google OR Microsoft OR OpenAI OR ChatGPT OR META OR ELON MUSK",
        language="en",
        page_size=20,
    )

    return jsonify(data)


@app.route("/news")
def get_news():
    data = client.get_everything(
        q="AI OR Google OR Microsoft OR OpenAI OR ChatGPT OR META OR LLM OR ELON MUSK",
        language="en",
        sort_by="publishedAt",
        page_size=20,
    )

    return jsonify(data)


if __name__ == "__main__":
    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True
    )