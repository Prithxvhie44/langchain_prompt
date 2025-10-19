from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os

load_dotenv()

chat_history=[]

api_key = os.getenv("GEMINI_API_KEY")
model=ChatGoogleGenerativeAI(api_key=api_key, model="gemini-2.5-flash")

while True:
    user_input = input("Enter your message (or 'exit' to quit): ")
    chat_history.append(user_input)
    if user_input.lower() == 'exit':
        break
    result=model.invoke(chat_history)
    chat_history.append(result.content)
    print("Response:", result.content)

print(chat_history)