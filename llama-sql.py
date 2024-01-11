from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

def start():
    uvicorn.run("main:app", host="127.0.0.1", port=5000, log_level="info")