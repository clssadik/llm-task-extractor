from pydantic import BaseModel,EmailStr,ValidationError, Field
from datetime import datetime, UTC
from functools import partial
from typing import Literal

class User(BaseModel):
    uid: int
    username: str
    email: EmailStr
    verified_at: datetime | None = None
    age: int
    bio: str = ""                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           
    is_active: bool = True
    gender: str | None = None

# user1 = User(uid=1,username="clssadik",email="cillsadik@gmail.com",age=23)
# print(user1.model_dump_json(indent=2))

try:
    user1 = User(uid=12)
except ValidationError as e:
    print(e)


class BlogPost(BaseModel):
    title: str
    content: str
    view_count: int = 0
    is_published: bool = False

    tags: list[str] = Field(default_factory=list)
    create_at = datetime = Field(default_factory=partial(datetime.now, tz = UTC))
    status: Literal["draft","published","archived"] = "draft"