
from app.features.feature_engineering import build_features
from app.models.model_loader import load_model

model = load_model()

def score_user(data):
    features = build_features(data)
    prob = model.predict_proba([features])[0][1]
    score = int(prob * 1000)

    reasons = []
    if features[2] > 5000:
        reasons.append("Good savings")
    if features[3] > 1:
        reasons.append("Late payments detected")

    return {
        "credit_score": score,
        "risk": "LOW" if score > 700 else "MEDIUM" if score > 500 else "HIGH",
        "reasons": reasons
    }
