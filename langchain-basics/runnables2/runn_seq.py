from pyexpat import model

from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv("../.env")

model = ChatOpenAI(
    model="gpt-4.1-mini",
    temperature=0.3,
    max_tokens=150,
)
prompt1 = PromptTemplate(
    template="Write a joke about {topic}", input_variables=["topic"]
)


parser = StrOutputParser()

prompt2 = PromptTemplate(
    template="Explain the following joke - {text}", input_variables=["text"]
)

chain = RunnableSequence(prompt1, model, parser, prompt2, model, parser)

print(chain.invoke({"topic": "AI"}))
