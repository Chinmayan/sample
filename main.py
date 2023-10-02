
from typing import List
from models import User,Gender,Role
from uuid import uuid4
from fastapi import FastAPI

app = FastAPI()

db: List[User]= [
    User(
        id = uuid4(),
        first_name = "Chinmaya",
        last_name = "Nanda",
        gender = Gender.male,
        roles = [Role.student]
    ),
    User(
        id = uuid4(),
        first_name = "Tanmaya",
        last_name = "Nanda",
        gender = Gender.male,
        roles = [Role.admin]
    ),
    User(
        id = uuid4(),
        first_name = "Geetanjali",
        last_name = "Das",
        #middle_name = "Gaydhar",
        gender = Gender.female,
        roles = ["user"]
    )

]

@app.get("/")
def root():
    return {"welcome":"chinmaya"}

@app.get("/api/v2/users")
async def users():
    return db


