# RunnableLambda is a LangChain Runnable primitive that converts a normal Python function
# into a Runnable component, allowing it to be used inside
# LCEL (LangChain Expression Language) chains.
# It helps developers add custom logic between different steps of an AI pipeline,
# such as modifying inputs, formatting outputs, validating data, calling external
# APIs, or applying business rules.

# RunnableLambda receives an input, executes the provided Python function,
# and passes the returned output to the next step in the chain.


from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import (
    RunnableSequence,
    RunnableParallel,
    RunnablePassthrough,
    RunnableLambda,
)

load_dotenv("../.env")

model = ChatOpenAI(model="gpt-4.1-mini", temperature=0.2, max_tokens=250)


def word_count(text):
    return len(text.split())


prompt = PromptTemplate(
    template="Write a joke about {topic}", input_variables=["topic"]
)

parser = StrOutputParser()

joke_gen_chain = RunnableSequence(prompt, model, parser)

parallel_chain = RunnableParallel(
    {"joke": RunnablePassthrough(), "word_count": RunnableLambda(word_count)}
)

final_chain = RunnableSequence(joke_gen_chain, parallel_chain)

result = final_chain.invoke({"topic": "AI"})

final_result = """{} \n word count - {}""".format(result["joke"], result["word_count"])

print(final_result)
