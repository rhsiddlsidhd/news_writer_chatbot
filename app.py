import streamlit as st
from chain import news_chain

st.title("News Writer")
st.caption("주제를 입력하면 뉴스 기사를 자동으로 작성합니다.")

topic = st.text_area("주제 입력", placeholder="예) 서울시 대중교통 요금 인상 계획", height=120)

if st.button("기사 생성", disabled=not topic.strip()):
    with st.spinner("기사 작성 중..."):
        result = news_chain.invoke({"topic": topic})
        st.session_state["article"] = result.content

if "article" in st.session_state:
    lines = st.session_state["article"].split("\n", 2)
    headline = lines[0].replace("헤드라인: ", "").strip()
    body = lines[2].strip() if len(lines) > 2 else ""

    st.divider()
    st.subheader(headline)
    st.write(body)
