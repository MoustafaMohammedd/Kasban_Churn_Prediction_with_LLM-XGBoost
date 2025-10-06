import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from src.utils.data_preprocessing_pipeline import X_train_final, y_train , X_test_final, y_test
import joblib
from sklearn.metrics import  classification_report

xgb_model = joblib.load('D:\Kasban_Churn_LLM\src\models\model_XGBoost.pkl')


X_train_pred=xgb_model.predict(X_train_final)

y_pred_test = xgb_model.predict(X_test_final)  

train_report = classification_report(y_train, X_train_pred)
print(f"Train Report \n {train_report}")
print("**"*40)

test_report = classification_report(y_test, y_pred_test)
print(f"Test_report \n {test_report}")