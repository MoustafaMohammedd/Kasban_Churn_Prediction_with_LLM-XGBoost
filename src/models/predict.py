import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from src.utils.data_preprocessing_pipeline import preprocess_new
import joblib
import pandas as pd

xgb_model = joblib.load('src/models/model_XGBoost.pkl')

def predict_churn(input_data) :
 
    processed_data = preprocess_new(input_data)
 
    prediction = xgb_model.predict(processed_data)
    
    return prediction

if __name__ == "__main__":
    
   sample_data = [
      ["Male", "No", "No", "No", 66, "Yes", "No", "Fiber optic", "Yes", "No", "Yes",
      "Yes", "Yes", "Yes", "Two year", "Yes", "Bank transfer (automatic)", 105.65, 6844.5]
   ]

   columns = ['gender', 'SeniorCitizen', 'Partner', 'Dependents', 'tenure',
            'PhoneService', 'MultipleLines', 'InternetService', 'OnlineSecurity',
            'OnlineBackup', 'DeviceProtection', 'TechSupport', 'StreamingTV',
            'StreamingMovies', 'Contract', 'PaperlessBilling', 'PaymentMethod',
            'MonthlyCharges', 'TotalCharges']

   df_sample = pd.DataFrame(sample_data, columns=columns)
   
   prediction = predict_churn(df_sample)
   print(prediction)
   print("Churn Prediction:", "Yes" if prediction[0] == 1 else "No") 