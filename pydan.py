from pydantic import BaseModel,ValidationError
from typing import List,Literal
from datetime import date

class Task(BaseModel):
    description: str
    priority: Literal["high","medium","low"]
    responsible: str | None = None
    due_date: date | None = None

class MeetingSummary(BaseModel):
    summary: str
    tasks: List[Task]

class Pydan:

    def __init__(self,data):
        self.data = data
    
    def parse(self):
        try:
            return MeetingSummary.model_validate(self.data)
        except ValidationError as e:
            print(e)

    
    