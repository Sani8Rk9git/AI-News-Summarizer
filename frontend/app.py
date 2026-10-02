import streamlit as st
import requests

st.set_page_config(page_title="AI News Summarizer", initial_sidebar_state="collapsed", layout="wide")

st.title("AI News Summarizer")
with st.form("summary_form"):
    article = st.text_area("News Article", height=200, placeholder="Paste your news article here...")
    submitted1 = st.form_submit_button("Summarize", use_container_width=True)

if submitted1:
    if not article.strip():
        st.warning("Please paste an article.")

    else:
        data = {
            "article":article
        }

        try:
            with st.container(border=True):
                with st.spinner("Summarizing..."):
                    response = requests.post("http://127.0.0.1:8000/summary", json=data)
                    response.raise_for_status()
                    result = response.json()
                    ai_response = result["response"]
                    # st.header("Generated Summary:")
                    # st.write("")
                    # st.write(ai_response)

                    st.session_state.summary = ai_response
                    st.session_state.article = article
                    st.session_state.article_analyzed = True
                    st.session_state.messages = []

        except requests.exceptions.RequestException as e:
            st.error(f"Could not connect to the backend: {e}")

if st.session_state.get("article_analyzed", False):
    with st.container(border=True):
        st.header("Generated Summary: ")
        st.write(st.session_state.summary)

    st.divider()

    st.header("Chat with the article")
    for message in st.session_state.messages:
        with st.chat_message(message["role"], avatar=None, width="content"):
            st.write(message["content"])

    user_input = st.chat_input("Ask Anything")

    if user_input:

        st.session_state.messages.append({
        "role": "user",
        "content":user_input
        })

        with st.chat_message("user"):
            st.write(user_input)

        try:
            with st.chat_message("assistant"):
                with st.spinner("Thinking..."):
                    response2 = requests.post("http://127.0.0.1:8000/ask",json={"question": user_input})
                    response2.raise_for_status()
                    result2 = response2.json()
                    answer = result2["answer"]
                    st.write(answer)

            st.session_state.messages.append({
                "role":"assistant",
                "content": answer
            })

        except requests.exceptions.RequestException as e:
            st.error(f"Could not connect to the backend: {e}")


