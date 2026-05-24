from enum import Enum
from fastapi import FastAPI

app = FastAPI()

class PaymentMethod(str, Enum):
    card = "card"
    cash = "cash"
    mobile_money = "mobile_money"

# # Task 1
# Create GET /products/{product_id} where product_id is an int
# Return {"product_id": product_id, "message": "Product found"}
# Test with a valid number and with a string like "abc" — observe the error

@app.get("/products/{product_id}")
async def get_product(product_id: int):
    return {"product_id": product_id, "message": "Product found"}

# # Task 2
# Create two endpoints:
# GET /users/me → returns {"user": "current logged in user"}
# GET /users/{user_id} → returns {"user_id": user_id}
# Make sure /users/me works correctly and doesn't get swallowed by the dynamic route
# Test both in the browser

@app.get("/users/me")
async def get_my_user():
    return {"user": "current logged in user"}

@app.get("/users/{user_id}")
async def get_my_user(user_id):
    return {"user_id": user_id}

# # Task 3
# Create an Enum called PaymentMethod with values:
# "card", "mobile_money", "cash"
# Create GET /payments/{method} that:
# - Returns {"method": method, "fee": "2%"} for card
# - Returns {"method": method, "fee": "1%"} for mobile_money
# - Returns {"method": method, "fee": "0%"} for cash
# Open /docs and confirm the dropdown shows exactly three options
# Test with an invalid method like "crypto" and observe the rejection

@app.get("/payments/{method}")
async def get_payment_details(method: PaymentMethod):
    if method is PaymentMethod.card:
        return {"method": method, "fee": "2%"}
    if method is PaymentMethod.mobile_money:
        return {"method": method, "fee": "1%"}
    return {"method": method, "fee": "0%"}

# # Task 4
# Create GET /users/{user_id}/orders/{order_id}
# Both parameters should be integers
# Return a dict with both values
# Test with /users/3/orders/99

@app.get("/users/{user_id}/orders/{order_id}")
async def get_user_order(user_id: int, order_id: int):
    return {"user_id": user_id, "order_id": order_id}