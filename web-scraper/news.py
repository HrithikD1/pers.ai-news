import streamlit as st
import newsapi
import requests


st.set_page_config(
    page_title="AI News Fetcher",
    page_icon="🤖",
    layout="wide",
)


api_key = st.secrets["NEWSAPI_KEY"]


def get_sources(api_key):
    sources_data = requests.get(
        f"https://newsapi.org/v2/top-headlines/sources?apiKey={api_key}"
    )
    sources_data.raise_for_status()

    with open("sources.json", "w") as f:
        f.write(sources_data.text)

    return sources_data.json()


def read_sources():
    with open("sources.json", "r") as f:
        return f.read()
    

sources = get_sources(api_key)

client = newsapi.NewsApiClient(
    api_key=api_key
)


st.title("🤖 AI News Fetcher")
st.write(
    "Stay up to date with the latest developments in artificial intelligence and technology."
)


st.divider()

st.header("🔥 Latest AI & Technology News")


with st.spinner("Fetching the latest tech news..."):
    top_news = client.get_everything(
        q="AI OR Google OR Microsoft OR OpenAI OR ChatGPT OR META OR LLM OR ELON MUSK",
        language="en",
        sort_by="publishedAt",
        page_size=20,
    )

    for article in top_news["articles"]:
        title = article.get("title", "Untitled article")
        description = article.get(
            "description",
            "No description available."
        )
        url = article.get("url", "#")
        source = article.get("source", {}).get(
            "name",
            "Unknown source"
        )
        published = article.get("publishedAt", "")

        if published:
            published = published[:10]

        with st.container(border=True):
            st.subheader(title)
            st.caption(f"📰 {source} • 📅 {published}")

            if description:
                st.write(description)

            st.link_button(
                "Read article →",
                url
            )


st.divider()

st.header("📰 Sources")

with st.expander("View available news sources"):
    with open("sources.json", "rb") as file:
        st.download_button(
            label="⬇️ Download sources.json",
            data=file,
            file_name="sources.json",
            mime="application/json"
        )

    if st.button("View Sources"):
        st.json(sources)