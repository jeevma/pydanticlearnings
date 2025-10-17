from pydantic import BaseModel, model_validator, field_validator, computed_field  # type: ignore

class User(BaseModel):
    username: str
    last_name: str
    age: int
    
    @field_validator("username")
    def username_length(cls, v):
        if len(v) < 4:
            raise ValueError("Username must be at least 4 characters long")
        return v
    
    
user_data = {
    "username": "joh",
    "last_name": "Doe",
    "age": 30,
}

try:
    u = User(**user_data)
except ValueError as e:
    print(e)    

##########################--Model Validator--################################
class SignupData(BaseModel):
    login_email: str
    password: str
    confirm_password: str   

    @model_validator(mode="after")
    def password_match(cls, values):
        if values.password != values.confirm_password:
            raise ValueError("Passwords do not match")
        return values
    
##########################--Computed Field --################################  

class Product(BaseModel):
    name: str
    price: float
    quantity: int

    @computed_field
    @property
    def total_cost(self) -> float:
        return self.price * self.quantity  
    
    
    
    