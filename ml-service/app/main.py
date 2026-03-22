
from fastapi import FastAPI
from app.services.scoring import score_user

app = FastAPI()

@app.post("/predict")
def predict(data: dict):
    return score_user(data)
