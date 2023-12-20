from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def hello_world():
    return "USN: 4NI20CS079"
