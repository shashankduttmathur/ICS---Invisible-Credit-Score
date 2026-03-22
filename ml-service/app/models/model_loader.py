
import joblib, os
from sklearn.ensemble import RandomForestClassifier

MODEL_PATH = "app/models/model.pkl"

def load_model():
    if os.path.exists(MODEL_PATH):
        return joblib.load(MODEL_PATH)
    return RandomForestClassifier().fit([[0,0,0,0,0]], [0])
