from langchain_core.messages import AIMessageChunk, SystemMessage
from graph import graph
from prompts import SYSTEM_PROMPT

topic = "서울 월드컵 경기장 잔디 문제"

inputs = [SystemMessage(content=SYSTEM_PROMPT.format(topic=topic))]

for msg, metadata in graph.stream({'messages':inputs},stream_mode='messages'):
    if isinstance(msg,AIMessageChunk):
        print(msg.content,end='')

