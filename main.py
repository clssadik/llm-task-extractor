from llm import LLM
from pydan import Pydan
import json

with open("prompt.txt", "r", encoding="utf-8") as prompt:
    system = prompt.read()

with open("user.txt", "r", encoding="utf-8") as f:
    user = f.read()

api = LLM(user=user,system=system)

success = False
for i in range(3):
    try:
        data = api.get_response()
        answer = data["choices"][0]["message"]["content"]
    
        verify = Pydan(data=answer)
        response_verify = verify.parse()
        success = True
        break

    except Exception as e:
        print(f"{i+1}. deneme başarısız: {e}")

if not success:
    print("3 denemede de başarısız olundu.")





