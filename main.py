from pydantic import BaseModel

class User(BaseModel):
    name: str
    email: str
    account_id: int

user = User(name="sadik",email="cillsadik@gmail.com",account_id=1)
print(user)