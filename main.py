from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def index():
    return {"h1": "Hello world!"}


users = ["Admin", "User1", "User2"]

@app.get("/read_users/")
def read_all_users():
    return {"all users": users}

@app.post("/add_user/{name}", status_code=200)
def add_users(name):
    if name in users:
        return {"message": f"Name {name} is exists "}
    users.append(name)
    return {"name": name}

@app.delete("/delete_user/{name}", status_code=200)
def delete_users(name):
    if name not in users:
        return {"message": f"Name {name} is not found "}
    users.remove(name)
    return {"name": name}
