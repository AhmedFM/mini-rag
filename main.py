from fastapi import FastAPI
app = FastAPI()

@app.get("/welcom") # Decorator
def welcome(): 
  return {
    "message": "Hello World!"
  }