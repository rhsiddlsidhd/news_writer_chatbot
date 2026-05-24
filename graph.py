from typing import Literal
from langgraph.graph import StateGraph, START, END
from langgraph.prebuilt import ToolNode
from langchain_core.messages import AIMessage
from state import State
from chain import generate
from tools import tools


def route_tools(state: State) -> Literal["tools", END]:
    """
    마지막 메시지에 도구 호출이 있는 경우 ToolNode로 라우팅하고,
    그렇지 않은 경우 끝으로 라우팅하기 위해 condition_edge에서 사용합니다.
    """
    if messages := state.get('messages', []):
        ai_message = messages[-1]
    else:
        raise ValueError(f'tool_edge 입력 상태에서 메시지를 찾을 수 없습니다.: {state}')
    if isinstance(ai_message, AIMessage) and len(ai_message.tool_calls) > 0:
        return 'tools'
    return END

graph_builder = StateGraph(State)
graph_builder.add_node("generate", generate)
tool_node = ToolNode(tools=tools)
graph_builder.add_node("tools", tool_node)

graph_builder.add_edge(START, "generate")
graph_builder.add_conditional_edges("generate", route_tools,{'tools':'tools',END:END})
graph_builder.add_edge("tools", "generate")

graph = graph_builder.compile()

