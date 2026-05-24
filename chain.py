from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from tools import tools
from state import State

load_dotenv()

_llm = ChatOpenAI(model="gpt-4.1-mini", temperature=0.7)

_llm_with_tools = _llm.bind_tools(tools)

def generate(state:State):
    """
    주어진 상태를 기반으로 챗봇의 응답 메시지를 생성합니다.

    매개변수:
    state (State): 현재 대화 상태를 나타내는 객체로, 이전 메시지들이 포함되어 있습니다.

    반환값:
    dict: 모델이 생성한 응답 메시지를 포함하는 딕셔너리
        형식은 {"messages":[응답 메시지]} 입니다.
    """
    return {"messages":_llm_with_tools.invoke(state['messages'])}
