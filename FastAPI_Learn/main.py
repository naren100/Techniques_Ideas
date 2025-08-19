# FastAPI is a python class that provides functionality for the api
from fastapi import FastAPI
from secondary import router as secondary_router


app = FastAPI()
app.include_router(secondary_router)

#======================
# TEST 1
# ======================
# async def root():
#   return {"message": "Hello World"}

#======================
# TEST 2
# ======================

#@app.get("/items/{item_id}")
# async def read_item(item_id):
    #return {"item_id": item_id}

#======================
# TEST 3
# ======================
#@app.get("/items/{item_id}")
#async def read_item(item_id: int):
    #return {"item_id": item_id}


@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}

@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}

@app.get("/")
async def root():
    # Show all posted items on the home page
    return {
        "message": "API is running"
    }


