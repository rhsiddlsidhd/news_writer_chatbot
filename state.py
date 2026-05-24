from typing import Annotated
from langgraph.graph.message import add_messages
from typing_extensions import TypedDict

class State(TypedDict):
    """
    State 클래스는 TypedDict 를 상속받습니다.
    속성:
        messages: Annotated[list, add_messages]: 메시지들은 "list" 타입을 가집니다.
        주석에 있는 'add_messages' 함수는 이 상태 키가 어떻게 업데이트되어야 하는지를 정의합니다.
        (이 경우, 메시지를 덮었쓰는 대신 리스트에 추가합니다)
    """
    messages: Annotated[list, add_messages]