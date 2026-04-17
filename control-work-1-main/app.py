from fastapi import FastAPI
from fastapi.responses import FileResponse
from models import User, Feedback

app = FastAPI()

user_instance = User(name="КимА", id=1)

feedbacks = []

@app.get("/")
def read_root():
    return FileResponse("index.html")

@app.get("/users")
def get_user():
    return user_instance

@app.post("/feedback")
def create_feedback(feedback: Feedback):
    feedbacks.append(feedback)
    return {"message": f"Feedback received. Thank you, {feedback.name}."}
