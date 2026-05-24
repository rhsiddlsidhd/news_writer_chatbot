from dotenv import load_dotenv
from langchain_core.messages import AIMessageChunk, SystemMessage
from prompts import SYSTEM_PROMPT
import streamlit as st

load_dotenv()


@st.cache_resource
def load_graph():
    from graph import graph
    return graph


def stream_article(topic: str):
    graph = load_graph()
    inputs = [SystemMessage(content=SYSTEM_PROMPT.format(topic=topic))]
    config = {"recursion_limit": 10}
    for msg, _ in graph.stream({'messages': inputs}, config=config, stream_mode='messages'):
        if isinstance(msg, AIMessageChunk) and msg.content:
            yield msg.content


st.title("News Writer Chatbot")

topic = st.text_input("기사 주제를 입력하세요", placeholder="예: 서울 월드컵 경기장 잔디 문제")

if st.button("기사 생성", type="primary"):
    if not topic.strip():
        st.warning("주제를 입력해주세요.")
    else:
        with st.spinner("기사를 작성하는 중입니다..."):
            st.write_stream(stream_article(topic))
