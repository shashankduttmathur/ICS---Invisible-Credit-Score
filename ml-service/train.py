
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib, os

os.makedirs("app/models", exist_ok=True)

data = pd.DataFrame({
 "income":[20000,50000,30000],
 "expenses":[15000,20000,25000],
 "savings":[2000,10000,3000],
 "late":[1,0,2],
 "target":[0,1,0]
})

data["ratio"] = data["expenses"]/data["income"]

X = data[["income","expenses","savings","late","ratio"]]
y = data["target"]

model = RandomForestClassifier()
model.fit(X,y)

joblib.dump(model, "app/models/model.pkl")
print("Model trained")
