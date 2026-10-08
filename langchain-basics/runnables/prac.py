# with help of llm and prompt write a poem
from abc import ABC, abstractmethod
import random

from langchain_core import runnables


class Runnable(ABC):
    @abstractmethod
    def invoke(input_data):
        pass


# createing llm
class NukliLLM(Runnable):
    def __init__(self):
        print("LLM Created")

    def invoke(self, prompt):
        response_list = [
            "Delhi is the capital of India",
            "IPL is a cricket league",
            "AI stands for Artificial Intelligence",
        ]
        return {"response": random.choice(response_list)}

    def predict(self, prompt):
        response_list = [
            "Delhi is the capital of India",
            "IPL is a cricket league",
            "AI stands for Artificial Intelligence",
        ]
        return {"response": random.choice(response_list)}


# creating prompt
class NakliPromptTemplate(Runnable):
    def __init__(self, template, input_variables):
        self.template = template
        self.input_variables = input_variables

    def invoke(self, input_dict):
        return self.template.format(**input_dict)

    def format(self, input_dict):
        return self.template.format(**input_dict)


template = NakliPromptTemplate(
    template="write a {length} poem about {topic}", input_variables=["length", "topic"]
)
prompt = template.format({"length": "short", "topic": "india"})
print(format)

# llm = NukliLLM()
# print(llm.predict(prompt))


# Now we create a chain where llm and prompt are i/p's
class NukliLLMChain:  # before adding Runnnable class
    def __init__(self, llm, prompt):
        self.llm = llm
        self.prompt = prompt

    def run(self, input_dict):
        final_prompt = self.prompt.format(input_dict)
        result = self.llm.predict(final_prompt)

        return result["response"]


llm = NukliLLM()
template = NakliPromptTemplate(
    template="write a {length} poem about {topic}", input_variables=["length", "topic"]
)

chain = NukliLLMChain(llm, template)
print(chain.run({"length": "short", "topic": "india"}))


class RunnableConnector(Runnable):
    def __init__(self, runnabe_list):
        self.runnabe_list = runnabe_list
