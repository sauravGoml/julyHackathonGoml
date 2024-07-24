from pydantic import BaseModel
from typing import List, Optional

class EmployeeCreate(BaseModel):
    first_name: str
    last_name: str
    email: str
    is_manger: Optional[bool] = False
    department_id: int

class EmployeeResponse(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: str
    is_manger: bool
    department_id: int

    class Config:
        orm_mode = True

class DepartmentCreate(BaseModel):
    name: str

class DepartmentResponse(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True