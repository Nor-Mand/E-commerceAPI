from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class User(BaseModel):
    id: str
    username: str
    password: str
    create_at: datetime = datetime.now()
    write_at: Optional[datetime]