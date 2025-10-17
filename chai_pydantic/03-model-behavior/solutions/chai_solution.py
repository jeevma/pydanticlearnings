from pydantic import BaseModel, computed_field, Field  # type: ignore

# TODO: Create a Booking model with the following fields:
# - user_id: int, required, not nullable
# - room_id: int, required, not nullable
# - nights: int (must be >= 1)
# - rate_per_night: float (must be >= 0)
# - total_cost: float (computed field, rate_per_night * nights)

class Booking(BaseModel):
    user_id: int
    room_id: int
    nights: int = Field(..., ge=1)
    rate_per_night: float = Field(..., ge=50)
    
    @computed_field
    @property
    def total_cost(self) -> float:
        return self.rate_per_night * self.nights
    
booking_data = {
    "user_id": 1,
    "room_id": 2,
    "nights": 5,
    "rate_per_night": 40,
}

b = Booking(**booking_data)
print(b)    