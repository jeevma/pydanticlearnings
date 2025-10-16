from pydantic import BaseModel, ValidationError

class Person(BaseModel):
    first_name: str
    last_name: str
    age: int
    city: str
    isActive: bool
    
input_data = {
    "first_name": "John",
    "last_name": "Doe",
    "age": 30,
    "city": "New York",
    "is_active": True
}    

#try:
p = Person(**input_data)
print(p)
#except ValidationError as e:
#    print(e)