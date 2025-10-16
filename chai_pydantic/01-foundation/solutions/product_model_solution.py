from pydantic import BaseModel

# TODO: Create a Product model with the following fields:
# - id: int, required, not nullable
# - name: str, required, not nullable
# - price: float, required, not nullable
# - quantity: int, required, not nullable
# - in_stock: bool, required, not nullable

class Product(BaseModel):
    id: int
    name: str
    price: float
    quantity: int
    in_stock: bool = True
    
data = {
    "id": 1,
    "name": "Product 1",
    "price": 10.99,
    "quantity": 10,
}

p = Product(**data)
print(p)    