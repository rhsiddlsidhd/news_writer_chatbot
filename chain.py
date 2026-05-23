from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from prompts import news_prompt

load_dotenv()

_llm = ChatOpenAI(model="gpt-4.1-mini", temperature=0.7)

news_chain = news_prompt | _llm
