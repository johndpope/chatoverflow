from revChatGPT.V1 import Chatbot
from dotenv import load_dotenv
import os

load_dotenv()

chatbot = Chatbot(config={
    "email": os.getenv(OPENAI_EMAIL),
    "password": os.getenv(OPENAI_PASSWORD)
})

prompt = input("What do you want to code today? \n\n")
response = ""

for data in chatbot.ask(
  prompt
):
    response = data["message"]

print("\n\n" + response + "\n\n")