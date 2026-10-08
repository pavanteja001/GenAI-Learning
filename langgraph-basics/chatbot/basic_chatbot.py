from typing import TypedDict, Annotated
from pathlib import Path

from dotenv import load_dotenv
from langchain_core.messages import BaseMessage, HumanMessage
from langchain_openai import ChatOpenAI
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from langgraph.checkpoint.memory import InMemorySaver

env_path = Path(__file__).resolve().parents[2] / ".env"  # GenAI-Learning/.env
load_dotenv(env_path)


class ChatState(TypedDict):
    # why BaseMessage bec we talk to llm in terms of msgs i.e capital of india this is Humanmsg
    # then Dlehi is AI msg, other are sys msg and tool msg so total we have 4
    # add_messages is the reducer: new msgs get appended to the list instead of replacing it
    messages: Annotated[list[BaseMessage], add_messages]


llm = ChatOpenAI(model="gpt-4.1-mini")


def chat_node(state: ChatState) -> ChatState:
    # send the full conversation so far to the llm, return only the new AI msg
    response = llm.invoke(state["messages"])
    return {"messages": [response]}


def build_chatbot():
    graph = StateGraph(ChatState)
    graph.add_node("chat_node", chat_node)
    graph.add_edge(START, "chat_node")
    graph.add_edge("chat_node", END)

    # checkpointer saves the state after every run, so the bot remembers old msgs
    return graph.compile(checkpointer=InMemorySaver())


def main():
    chatbot = build_chatbot()

    # thread_id identifies one conversation; same id = same memory
    config = {"configurable": {"thread_id": "1"}}

    while True:
        user_message = input("You: ")
        if user_message.strip().lower() in ["exit", "quit", "bye"]:
            break

        result = chatbot.invoke(
            {"messages": [HumanMessage(content=user_message)]}, config=config
        )
        print("AI:", result["messages"][-1].content)

    # see everything the checkpointer stored for this thread
    for message in chatbot.get_state(config).values["messages"]:
        print(f"{message.type}: {message.content}")


if __name__ == "__main__":
    main()
