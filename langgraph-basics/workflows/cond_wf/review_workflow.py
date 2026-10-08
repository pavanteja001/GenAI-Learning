from unittest.mock import sentinel

from langgraph.graph import StateGraph, START, END
from langchain_openai import ChatOpenAI
from typing import TypedDict, Literal
from dotenv import load_dotenv, find_dotenv
from pydantic import BaseModel, Field
import os

load_dotenv(find_dotenv())
# print(os.getenv("OPENAI_API_KEY"))

model = ChatOpenAI(model="gpt-4o-mini")


#class SentimentSchema(BaseModel):
     
    # Literal -strictest kind of type. Instead of "any string," it means "only one of these exact strings.
    # Field() attaches metadata to the field. The description isn't a code comment — it becomes part of the schema Pydantic generates, and that schema gets sent to the language model.


#class DiagnosisSchema(BaseModel):
 #   issue_type: Literal["UX", "Performance", "Bug", "Support", "Other"] = Field(description='The category of issue mentioned in the review')
  #  tone: Literal["angry", "frustrated", "disappointed", "calm"] = Field(description='The emotional tone expressed by the user')
   # urgency: Literal["low", "medium", "high"] = Field(description='How urgent or critical the issue appears to be')


#structured_model = model.with_structured_output(SentimentSchema)
#structured_model2 = model.with_structured_output(DiagnosisSchema)

#prompt = 'What is the sentiment of the following review - The software too good'
#structured_model.invoke(prompt).sentiment