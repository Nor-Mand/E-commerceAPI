from fastapi import APIRouter, HTTPException
from schemas.clients.schema_users import User
from uuid import uuid4 as uuid

users = APIRouter()

userData = []


# Get all users
@users.get('/users', tags=["Clients: Get methods"])
def get_users():
    return userData


# Get user by id
@users.get('/users/{user_id}', tags=["Clients: Get methods"])
def get_user_id(user_id: str):
    for user in userData:
        if user["id"] == user_id:
            return user
    raise HTTPException(status_code=404, detail="Not Found")


# Create user
@users.post('/users', tags=["Clients: Post methods"])
def create_user(user_id: User):
    user_id.id = str(uuid())
    userData.append(user_id.dict())
    return userData[-1]


# Delete user
@users.delete('/users/{user_id}', tags=["Clients: Delete methods"])
def delete_user(user_id: str):
    for index, user in enumerate(userData):
        if user["id"] == user_id:
            userData.pop(index)
        return{"message": f"The user {user['username']} was delete successfully"}
    raise HTTPException(status_code=404, detail="Not Found")


# Update user
@users.put('/users/{user_id}', tags=["Clients: Put methods"])
def update_user(user_id: str, update: User):
    for index, user in enumerate(userData):
        if user["id"] == user_id:
            userData[index]["username"] = update.username
            userData[index]["password"] = update.password
            userData[index]["write_at"] = update.write_at
            return{"message": f"The user with id: {user_id} was update successfully"}
    raise HTTPException(status_code=404, detail="Not Found")
