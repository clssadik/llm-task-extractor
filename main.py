from pydantic import BaseModel,EmailStr,ValidationError
from datetime import datetime

class User(BaseModel):
    username: str
    email: EmailStr
    age: int
    bio: str = ""
    is_active: bool = True
    gender: str | None = None

user1 = User(username="clssadik",email="cillsadik@gmail.com",age=23)
print(user1)