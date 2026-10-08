from dotenv import load_dotenv
from langgraph.graph import END, START, StateGraph
from langchain_openai import ChatOpenAI
from typing import TypedDict
import os
from pathlib import Path

env_path = Path(__file__).parent.parent / ".env"  # GenAI-Learning/.env
loaded = load_dotenv(env_path)
print("Loaded:", loaded, "from", env_path)
print(os.getenv("OPENAI_API_KEY"))


class LLMstate(TypedDict):
    question: str
    answer: str


model = ChatOpenAI(model="gpt-4.1-mini", temperature=0.2, max_tokens=150)


def llm_qa(state: LLMstate) -> LLMstate:
    question = state["question"]
    answer = model.invoke(question).content
    return {"answer": answer}


graph = StateGraph(LLMstate)
graph.add_node("llm_qa", llm_qa)
graph.add_edge(START, "llm_qa")
graph.add_edge("llm_qa", END)

workflow = graph.compile()

initialState = {"question": "Who is Virat Kohli"}
finalState = workflow.invoke(initialState)
print(finalState)
