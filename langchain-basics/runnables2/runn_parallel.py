# RunnableParallel is a runnable primitive that allows multiple runnables to execute in parallel.
# Each runnable receives the same input and processes it independently, producing a dictionary of outputs.


from langchain_core.runnables import RunnableSequence, RunnableParallel
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser

load_dotenv("../.env")

model = ChatOpenAI(model="gpt-4.1-mini", temperature=0.2, max_tokens=150)

parser = StrOutputParser()

prompt1 = PromptTemplate(
    template="write a linkedin post about {topic}", input_variables=["topic"]
)

prompt2 = PromptTemplate(
    template="write a tweet about {topic}", input_variables=["topic"]
)

parallel_chain = RunnableParallel(
    {
        "tweet": RunnableSequence(prompt1, model, parser),
        "linkedin": RunnableSequence(prompt2, model, parser),
    }
)

result = parallel_chain.invoke({"topic": "AI"})

print(result["tweet"])
print(result["linkedin"])
