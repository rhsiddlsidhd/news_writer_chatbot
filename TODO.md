# News Writer Chatbot — 시작 전 체크리스트

## 1. 기획

- [x] 입력/출력 스펙 정의
  - 입력: 기사 주제 (자유 텍스트)
  - 출력: 헤드라인 + 본문 (자유 형식)
- [x] 지원할 기사 유형 결정 → 제한 없음
- [x] 대화 흐름 정의 → 1회 생성 (채팅 히스토리 없음)

## 2. 기술 스택 확정

- [x] LLM: OpenAI GPT-4.1-mini
- [x] UI: Streamlit
- [x] 언어: Python (최신 버전)
- [x] 패키지 관리: `uv`
- [x] 검색: DuckDuckGo API (패키지 추가는 추후)

## 3. 환경 설정

- [x] `uv init` 으로 프로젝트 초기화
- [x] 의존성 설치 (`openai`, `langchain`, `langchain-openai`, `langchain-community`, `streamlit`, `python-dotenv`)
- [x] `.env` 파일 생성 및 `OPENAI_API_KEY` 등록 (수동으로 직접 생성)
- [x] `.gitignore` 작성 (`.env`, `__pycache__`, `.venv` 포함)

## 4. 프로젝트 구조 설계

- [x] 디렉토리 구조 결정 (`app.py`, `chain.py`, `prompts.py`)
- [x] Streamlit 상태 관리 방식 결정 (`st.session_state`로 생성 기사 저장)

## 5. 프롬프트 설계

- [ ] 시스템 프롬프트 초안 작성 (기자 페르소나, 기사 형식 규칙)
- [ ] 유저 입력 → 프롬프트 변환 템플릿 정의

## 6. 개발

- [ ] Streamlit UI 구현 (입력 폼, 생성 버튼, 결과 표시)
- [ ] OpenAI API 연동
- [ ] 뉴스 기사 생성 로직 구현

## 7. 테스트

- [ ] 다양한 주제로 기사 생성 품질 확인
- [ ] 엣지 케이스 테스트 (빈 입력 등)
- [ ] Streamlit 앱 실행 및 UI 동작 검증
