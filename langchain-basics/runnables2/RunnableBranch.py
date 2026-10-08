# RunnableBranch is a LangChain Runnable primitive used to create conditional workflows
# inside LCEL (LangChain Expression Language).
# It allows your AI pipeline to make decisions and choose different execution paths
# depending on the input, output, user query, or any custom condition.
# It works similar to if-elif-else programming logic, where each condition is checked
# in order and the runnable connected to the first True condition is executed.


from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import (
    RunnableSequence,
    RunnableParallel,
    RunnablePassthrough,
    RunnableBranch,
    RunnableLambda,
)

load_dotenv("../.env")

prompt1 = PromptTemplate(
    template="Write a detailed report on {topic}", input_variables=["topic"]
)

prompt2 = PromptTemplate(
    template="Summarize the following text \n {text}", input_variables=["text"]
)

model = ChatOpenAI(model="gpt-4.1-mini", temperature=0.2, max_tokens=250)

parser = StrOutputParser()

report_gen_chain = prompt1 | model | parser

branch_chain = RunnableBranch(
    (lambda x: len(x.split()) > 300, prompt2 | model | parser), RunnablePassthrough()
)

final_chain = RunnableSequence(report_gen_chain, branch_chain)

print(final_chain.invoke({"topic": "Russia vs Ukraine"}))
