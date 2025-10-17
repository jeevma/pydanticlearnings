from typing import Optional
from pydantic import BaseModel, Field

# TODO: Create an Employee model with the following fields:
# - id: int
# - name: str (min 3 characters)
# - department: optiona str (default 'General')
# - salary: float (must be >= 10000)

class Employee(BaseModel):
    id: int
    name: str = Field(
        ...,
        min_length=3,
        max_length=50,
        description="Name of the employee",
        json_schema_extra={"example": "John Doe"},
    )
    department: Optional[str] = None
    salary: float = Field(..., ge=10000)
    
emp_data = {
    "id": 1,
    "name": "John Doe",
    "salary": 10000,
}

e = Employee(**emp_data)
print(e)    