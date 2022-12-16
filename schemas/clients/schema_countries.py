from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class Countries(BaseModel):
    id: str
    name: str
    create_at: datetime = datetime.now()
    write_at: Optional[datetime]