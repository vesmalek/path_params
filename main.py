from enum import Enum
from fastapi import FastAPI

class PlanName(str, Enum):
    basic = "basic"
    pro = "pro"
    enterprise = "enterprise"

app = FastAPI()

@app.get("/products/{product_id}")
async def root(product_id: int):
    return {"product_id": product_id}

@app.get("/")
async def root():
    return {"message": "My API is working"}

@app.get("/plans/{plan_name}")
async def root(plan_name: PlanName):
    if plan_name is PlanName.basic:
        return {"plan_name": plan_name, "price": "$9/month"}
    if plan_name is PlanName.pro:
        return {"plan_name": plan_name, "price": "$29/month"}
    return {"plan_name": plan_name, "price": "$50/month"}