from pydantic import BaseModel # type: ignore

# TODO: Create a Booking model with the following fields:
# - user_id: int, required, not nullable
# - room_id: int, required, not nullable
# - nights: int (must be >= 1)
# - rate_per_night: float (must be >= 0)
# - total_cost: float (computed field, rate_per_night * nights)