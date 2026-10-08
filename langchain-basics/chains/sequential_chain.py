from pydoc_data import topics
from unittest import result

from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv("../.env")

parser = StrOutputParser()

prompt1 = PromptTemplate(
    template="Generate a detaailed report on {topic}",
    input_variables=["topic"]
)

prompt2 = PromptTemplate(
    template='Generate a 5 pointer summary from the following text \n {text}',
    input_variables=['text']
)

model = ChatOpenAI(
    model="gpt-4.1-mini",
    temperature=0.3,
    max_tokens = 150,
)

chain = prompt1 | model | parser | prompt2 | model | parser

result = chain.invoke({"topic" : "Unemployment in India"})

print(result)

chain.get_graph().print_ascii()
#chain.get_graph().draw_mermaid_png()