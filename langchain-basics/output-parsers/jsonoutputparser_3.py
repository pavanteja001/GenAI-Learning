from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv("../.env")

llm = ChatOpenAI(
    model="gpt-4.1-mini",
    temperature=0.3,
    max_tokens = 150,
)

parser = JsonOutputParser()

template = PromptTemplate(
    template='Give me 5 facts about {topic} \n {format_instruction}',
    input_variables=['topic'],
    partial_variables={'format_instruction': parser.get_format_instructions()}
)

chain = template | llm | parser

result = chain.invoke({'topic':'black hole'})

print(parser.get_format_instructions())#Return a JSON object.

print(result)

# partial_variables Explained
# What does parser.get_format_instructions() return?
# It returns a pre-written string that tells the LLM how to format its output. Something like:
# "Return your answer as a JSON object. Do not include any extra text outside the JSON block."
# You can think of it as the parser talking to the LLM on your behalf.

# What does partial_variables do?
# A normal variable like {topic} is filled in at runtime when you call chain.invoke(...).
# A partial_variable is filled in immediately when the template is created — it's hardcoded in, so you never have to pass it manually later.
# Without partial_variables, you'd have to do this every time:
# pythonchain.invoke({
#     'topic': 'black hole',
#     'format_instruction': parser.get_format_instructions()  # annoying to repeat
# })
# With partial_variables, you just do:
# chain.invoke({'topic': 'black hole'})  # format_instruction is already baked in