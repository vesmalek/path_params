from fastapi import FastAPI

app = FastAPI()

@app.get("/products/{product_id}")
async def root(product_id: int):
    return {"product_id": product_id}

@app.get("/")
async def root():
    return {"message": "My API is working"}