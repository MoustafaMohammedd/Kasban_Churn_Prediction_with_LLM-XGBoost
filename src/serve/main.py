from fastapi import FastAPI
import os
import sys
import pandas as pd
from pydantic import BaseModel
from dotenv import load_dotenv
load_dotenv(".env")
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from src.llm.extractor import extract_features
from src.models.predict import predict_churn



class ChurnRequest(BaseModel):
    text: str
    
    
app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the Customer Churn Prediction API"}

@app.post("/predict_churn")

def predict_churn_endpoint(data: ChurnRequest):

    
    features = extract_features(data.text)
    
    sample = pd.DataFrame([features])
    
    prediction = predict_churn(sample)
    
    return {"churn_prediction": "Yes" if prediction[0] == 1 else "No",
            "features": features}

