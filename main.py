import os
import requests
from dotenv import load_dotenv
load_dotenv()
from pydantic import BaseModel,ValidationError
from typing import List,Literal
from datetime import date

class Task(BaseModel):
    description: str
    priority: Literal["high","medium","low"]
    responsible: str
    due_date = date

class MeetingSummary(BaseModel):
    summary: str
    tasks: List[Task]

URL = "https://api.deepseek.com/chat/completions"

user = input("Request: ")

head_params = {
    "Authorization": f"Bearer {os.environ.get('DEEPSEEK_API_KEY')}",
    "Content-Type": "application/json",
}

json_params = {
    "model": "deepseek-v4-flash",
    "messages": [
        {"role": "system", "content": "Give the responses only as JSON files."},
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
        try:
            result = MeetingSummary.model_validate(data)
        except ValidationError as e:
            print(e)
except requests.exceptions.RequestException as e:
    print(f"Bağlantı hatası: {e}")
