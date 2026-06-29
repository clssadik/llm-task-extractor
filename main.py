from llm import LLM
from pydan import Pydan

with open("prompt.txt", "r", encoding="utf-8") as prompt:
    system = prompt.read()

user = input("Request: ")

data = LLM(user=user,system=system)
result = Pydan(data=data)


