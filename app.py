from fastapi import FastAPI
import joblib
import pandas as pd

app = FastAPI()

model = joblib.load("delivery_eta_model.pkl")


@app.get("/")
def home():
    return {"message": "Delivery ETA Prediction API"}


@app.post("/predict")
def predict(Distance_km: float,Traffic: str,Weather: str,Vehicle: str,Order_Size: int):
    data = pd.DataFrame([{
        "Distance_km": Distance_km,
        "Traffic": Traffic,
        "Weather": Weather,
        "Vehicle": Vehicle,
        "Order_Size": Order_Size
    }])

    prediction = model.predict(data)[0]

    return {
        "predicted_delivery_time_minutes": round(float(prediction), 2)
    }
