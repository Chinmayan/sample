from pydantic import BaseModel
from typing import Optional,List
from uuid import UUID, uuid4
from enum import Enum


class Gender(str,Enum):
    male = "male"
    female = "female"

class Role(str,Enum):
    user = "User"
    student = "Student"
    admin = "Admin"    
    
class User(BaseModel):
    id : Optional[UUID] = uuid4()
    first_name : str
    last_name : str
    #middle_name : Optional[str]
    gender :Gender
    roles : List[Role]

class UserUpdateRequest(BaseModel):
    first_name :Optional[str]
    last_name :Optional[str]
    roles :Optional[List[Role]]


    



