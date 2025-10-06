import sys
import os
import pandas as pd
from dotenv import load_dotenv
load_dotenv("D:\Kasban_Churn_LLM\.env")
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from src.llm.extractor import extract_features
from src.models.predict import predict_churn

text="""
A 31-year-old male, not senior, not has a partner but no dependents. 
He uses phone service with multiple lines. Internet is fiber optic with security, backup, 
device protection, and tech support all enabled. He streams both TV and movies. 
His contract is five years, paperless billing enabled, 
payment by credit card automatic. He has tenure of 10 months, 
monthly charges 12.5, total charges 315.0.
"""

text_2="""A 31-year-old male, not a senior citizen, doesn't have a partner and has no dependents.
He uses phone service with multiple lines. His internet service is fiber optic, with all add-ons enabled — including online security, backup, device protection, and tech support.
He actively streams both TV and movies.
His contract is only month-to-month, with paperless billing enabled, and payments made via electronic check.
He has a tenure of just 2 months, with monthly charges of 95.0, and total charges of only 190.0."""



features=extract_features(text_2)
print(features)

sample = pd.DataFrame([features])

prediction = predict_churn(sample)
print(prediction)
print("Churn Prediction:", "Yes" if prediction[0] == 1 else "No") 