import os
import requests
from dotenv import load_dotenv
load_dotenv()
from pydan import Pydan

URL = "https://api.deepseek.com/chat/completions"

with open("prompt.txt", "r", encoding="utf-8") as prompt:
    system = prompt.read()

user = input(requests)

head_params = {
    "Authorization": f"Bearer {os.environ.get('DEEPSEEK_API_KEY')}",
    "Content-Type": "application/json",
}

json_params = {
    "model": "deepseek-v4-flash",
    "messages": [
        {"role": "system", "content": system},
        {"role": "user", "content": user},
    ],
    "thinking": {"type": "enabled"},
    "reasoning_effort": "high",
    "temperature": 1,
    "top_p": 1,
    "max_tokens": 4096,
    "stream": False,
}

try:
    response = requests.post(URL, headers=head_params, json=json_params)
    if response.status_code == 401:
        print("API key geçersiz")
    else:
        response.raise_for_status()
        data = response.json()
        result = Pydan(data=data)
except requests.exceptions.RequestException as e:
    print(f"Bağlantı hatası: {e}")
