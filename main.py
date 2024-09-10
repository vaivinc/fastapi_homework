from fastapi import FastAPI, HTTPException

app = FastAPI()


@app.get("/")
def index():
    return {"h1": "Hello world!"}


users = ["Admin", "User1", "User2"]

@app.get("/read_users/")
def read_all_users():
    return {"all users": users}

@app.post("/add_user/{name}")
def add_users(name):
    if name in users:
        raise HTTPException(status_code=400, detail="User is already in the list")
    users.append(name)
    return {"name": name}

@app.delete("/delete_user/{name}")
def delete_users(name):
    if name not in users:
        raise HTTPException(status_code=400, detail="User is not found")
    users.remove(name)
    return {"name": name}
