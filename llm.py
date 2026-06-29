import os
import requests
from dotenv import load_dotenv
load_dotenv()

class LLM:
    
    def __init__(self,user,system):
        self.user = user
        self.system = system
    
    def get_response(self):
    
        URL = "https://api.deepseek.com/chat/completions"

        head_params = {
            "Authorization": f"Bearer {os.environ.get('DEEPSEEK_API_KEY')}",
            "Content-Type": "application/json",
        }

        json_params = {
            "model": "deepseek-v4-flash",
            "messages": [
                {"role": "system", "content": self.system},
                {"role": "user", "content": self.user},
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
                return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Bağlantı hatası: {e}")