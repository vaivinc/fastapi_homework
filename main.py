from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def index():
    return {"h1": "Hello world!"}


@app.get("/{name}+{name2}/")
def say_hello(name: int, name2: int):
    return {name + name2}


@app.get("/{name}-{name2}/")
def say_hello(name: int, name2: int):
    return {name - name2}


@app.get("/{name}*{name2}/")
def say_hello(name: int, name2: int):
    return {name * name2}


@app.get("/{name}/{name2}/")
def say_hello(name: int, name2: int):
    return {name / name2}
