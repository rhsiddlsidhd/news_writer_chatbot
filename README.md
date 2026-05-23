# News Writer Chatbot

주제를 입력하면 GPT-4.1-mini가 뉴스 기사(헤드라인 + 본문)를 자동으로 작성합니다.

## 기술 스택

- **LLM**: GPT-4.1-mini (OpenAI)
- **Framework**: LangChain
- **UI**: Streamlit
- **패키지 관리**: uv

## 실행 방법

```bash
# 의존성 설치
uv sync

# .env 파일 생성 후 API 키 입력
OPENAI_API_KEY=sk-...

# 앱 실행
uv run streamlit run app.py
```

## 프로젝트 구조

```
news_writer_chatbot/
├── app.py        # Streamlit UI
├── chain.py      # LangChain 체인
└── prompts.py    # 프롬프트 템플릿
```
