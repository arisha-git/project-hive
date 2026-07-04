from fastapi import FastAPI

app = FastAPI(title="ProjectHive API")

@app.get("/")
def home():
    return {
        "message": "Welcome to ProjectHive API!"
    }