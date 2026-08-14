import streamlit as st
import requests


BACKEND_URL = "http://127.0.0.1:5000"


st.set_page_config(
    page_title="AI News Fetcher",
    page_icon="🤖",
    layout="wide",
)


st.title("🤖 AI News Fetcher")
st.write(
    "Stay up to date with the latest developments in artificial intelligence and technology."
)


st.divider()

st.header("🔥 Latest AI & Technology News")


if st.button("Save Top Headlines"):
    response = requests.get(f"{BACKEND_URL}/headlines")
    response.raise_for_status()

    top_headlines = response.json()

    with open("top_headlines.txt", "w") as f:
        for article in top_headlines["articles"]:
            f.write(f"{article.get('title', 'Untitled article')}\n")
            f.write(f"{article.get('url', '#')}\n\n")


with st.spinner("Fetching the latest tech news..."):
    response = requests.get(f"{BACKEND_URL}/news")
    response.raise_for_status()

    top_news = response.json()

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
    response = requests.get(f"{BACKEND_URL}/sources")
    response.raise_for_status()

    sources = response.json()

    with open("sources.json", "wb") as file:
        file.write(response.content)

    st.download_button(
        label="⬇️ Download sources.json",
        data=response.content,
        file_name="sources.json",
        mime="application/json"
    )

    if st.button("View Sources"):
        st.json(sources)