from pydantic import BaseModel


class Customers(BaseModel):
    id: int
    user_id: int
    first_name: str
    last_name: str
    email: str
    address: str
    telephone: int
    country_id: int
    create_at: str
    write_at: str