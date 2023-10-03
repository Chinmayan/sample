from fastapi import FastAPI, HTTPException
from models import User,Role,Gender,UserUpdateRequest
from typing import List
from uuid import uuid4,UUID


app = FastAPI()

db:List[User] = [
    User(
        id = UUID("e95ec74e-1b69-4021-8c9b-6420d8dccf5f"),
        first_name = "chinmaya",
        last_name = "nanda",
        gender = Gender.male,
        roles = [Role.student]
    ),
        User(
        id = UUID("152d4cf4-664d-4696-a1a2-ced0763d9ea5"),
        first_name = "Tanmaya",
        last_name = "nanda",
        gender = Gender.male,
        roles = [Role.user]
        ),
        User(
        id = UUID("406e78c8-b723-4453-bf1c-3bceb9da8c0f"),
        first_name = "Geetanjai",
        last_name = "Das",
        gender = Gender.female,
        roles = [Role.admin]
        )
]

@app.get("/")
def root():
    return{"Welcome":"chinmaya"}

@app.get("/api/v2/users")
def users():
    return db

@app.post("/api/v2/users")
def register_user(user:User):
    db.append(user)
    return {user.id}

@app.delete("/api/v2/users/{user_id}")
def delete_user(user_id:UUID):
    for user in db:
        if user.id == user_id:
            db.remove(user)
            return 
    raise HTTPException(
        status_code= 404,
        detail=f"User with user id {user.id} do not exists"    
    )
@app.put("/api/v2/users/{user_id}")
async def update_user(user_update:UserUpdateRequest,user_id:UUID):
    for user in db:
        if user.id == user_id:
            if user_update.first_name is not None:
                user.first_name = user_update.first_name
            if user_update.last_name is not None:
                user.last_name = user_update.last_name    
            if user_update.roles is not None:
                user.roles = user_update.roles
            return 
    raise HTTPException(
        status_code= 404,
        detail=f"User with user id {user.id} do not exists"

    )    