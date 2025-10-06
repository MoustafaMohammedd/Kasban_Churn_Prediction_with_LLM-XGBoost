# 📊 Kasban Churn Prediction with LLM + XGBoost

This project combines **Large Language Models (LLMs)** with a **machine learning classifier** to predict customer churn.

Instead of manually filling structured forms, the user can **write free-form text** about a customer. The LLM extracts structured features (gender, internet service, contract type, etc.) using LangChain, and these features are passed into a trained **XGBoost churn prediction model**.

---

## 🚀 Features

* **LLM-based feature extraction**

  * Uses `langchain-openai` with `ChatOpenAI` to parse customer descriptions.
  * Extracts fields like gender, contract type, monthly charges, etc.
  * Validated against a strict **Pydantic schema** to ensure correctness.

* **Churn classification model**

  * Trained with **XGBoost** on the Telco Customer Churn dataset.
  * Preprocessing pipeline includes scaling numeric values and encoding categorical variables.

* **FastAPI service**

  * REST API endpoint (`POST /`) to send free-text input.
  * Returns both structured features and churn prediction (`Yes` / `No`).

---

## 📂 Project Structure

```
Kasban_Churn_LLM/
│
├── requirements.txt            # Python dependencies
├── .env.example                # Example environment variables
├── README.md                   # Project documentation
│
├── data/                       # Raw dataset
│   └── WA_Fn-UseC_-Telco-Customer-Churn.csv
│
├── src/
    ├── llm/                    # LLM extraction logic
    │   ├── schema.py           # Pydantic schema for customer features
    │   ├── extractor.py        # LangChain LLM + parser
    │   └── test.py             # Test LLM extraction
    │
    ├── models/                 # ML model training and inference
    │   ├── train_xgb.py        # XGBoost training script
    │   ├── predict.py          # Load trained model and predict
    │   ├── test.py             # Evaluate model performance
    │   └── model_XGBoost.pkl   # Saved trained model
    │
    ├── utils/                  # Data preprocessing pipeline
    │   └── data_preprocessing_pipeline.py
    │
    ├── serve/                  # Serving layer
    │   ├── main.py             # FastAPI application
    │   └── test_llm_with_xgb.py# Test full pipeline (LLM → XGB)
    │
    └── notebooks/              # Experiments
       └── EDA.ipynb
```

---

## ⚙️ Setup

### 1. Clone the repository

```bash
git clone https://github.com/MoustafaMohammedd/Kasban_Churn_Prediction_with_LLM-XGBoost.git
cd Kasban_Churn_Prediction_with_LLM-XGBoost
```

### 2. Create virtual environment & install dependencies

```bash
python -m venv venv
source venv/bin/activate    # On Linux/Mac
venv\Scripts\activate       # On Windows

pip install -r requirements.txt
```

### 3. Configure environment variables

Copy `.env.example` → `.env` and fill in:

```env
API_KEY="your_api_key"
BASE_URL="https://api.openai.com/v1"
MODEL_NAME="openai/gpt-oss-20b:free"
```

### 4. Train the churn model

```bash
python src/models/train_xgb.py
```

This will save the model as `src/models/model_XGBoost.pkl`.

---

## ▶️ Running the API

### Start FastAPI server

```bash
uvicorn src.serve.main:app --reload
```

### Test endpoint

POST request to `http://127.0.0.1:8000/docs

**Example input:**

```json
{
  "text": "A 45-year-old female with fiber optic internet, streaming TV, no partner, two dependents, contract month-to-month, paperless billing, tenure 12 months, monthly charges 70.5, total charges 846.0."
}
```

**Example output:**

```json
{
  "churn_prediction": "Yes",
  "features": {
    "gender": "Female",
    "SeniorCitizen": "No",
    "Partner": "No",
    "Dependents": "Yes",
    "tenure": 12,
    "PhoneService": "Yes",
    "MultipleLines": "No",
    "InternetService": "Fiber optic",
    "OnlineSecurity": "No",
    "OnlineBackup": "Yes",
    "DeviceProtection": "No",
    "TechSupport": "No",
    "StreamingTV": "Yes",
    "StreamingMovies": "No",
    "Contract": "Month-to-month",
    "PaperlessBilling": "Yes",
    "PaymentMethod": "Electronic check",
    "MonthlyCharges": 70.5,
    "TotalCharges": 846.0
  }
}
```

---

## 🧪 Testing

* Test LLM feature extraction only:

  ```bash
  python src/llm/test.py
  ```

* Test ML model predictions only:

  ```bash
  python src/models/test.py
  ```

* Test full pipeline (LLM → XGB → prediction):

  ```bash
  python src/serve/test_llm_with_xgb.py
  ```

```

---

## 📈 Next Steps

* Improve LLM prompt to handle missing or ambiguous customer details.
* Add more ML algorithms for comparison (LightGBM, CatBoost).
* Add a simple UI for non-technical users.

---

🔥 Now you have a full end-to-end pipeline:
**Free-text → LLM Feature Extraction → XGBoost Prediction → FastAPI Service**.


