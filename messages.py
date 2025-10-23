from langchain_core.messages import SystemMessage,HumanMessage,AIMessage
from langchain_google_genai import ChatGoogleGenerativeAI   
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
model=ChatGoogleGenerativeAI(api_key=api_key, model="gemini-2.5-flash")

messages=[
    SystemMessage(content="You are a helpful assistant"),
    HumanMessage(content="Tell me info about langchain")
]

result=model.invoke(messages)

messages.append(result.content)

print(messages)