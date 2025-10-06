import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from src.utils.data_preprocessing_pipeline import X_train_final, y_train
import numpy as np
from xgboost import XGBClassifier
from sklearn.model_selection import GridSearchCV, cross_val_score
import joblib


xgb = XGBClassifier(random_state=42)

params_best_xgb = {'n_estimators': np.arange(100, 200, 50), 'max_depth': np.arange(4, 15, 2), 
                   'learning_rate': [0.1, 0.2], 'subsample': [0.8, 0.9]}


grid_xgb = GridSearchCV(estimator=xgb, param_grid=params_best_xgb, cv=5, 
                        scoring='f1_weighted', n_jobs=-1, verbose=6)
grid_xgb.fit(X_train_final, y_train) 


best_xgb_params = grid_xgb.best_params_
print('best_xgb_params -- ', best_xgb_params)

best_xgb = grid_xgb.best_estimator_  
print('best_xgb -- ', best_xgb)


tuned_xgb = cross_val_score(estimator=best_xgb, X=X_train_final, y=y_train, 
                               cv=5, scoring='f1_weighted', n_jobs=-1)  

print(f'Scores Using Tuned Tuned XGBoost --- {np.round(tuned_xgb, 4)}')
print(f'Mean of Scores Using Tuned XGBoost --- {tuned_xgb.mean():.4f}')

joblib.dump(best_xgb, 'src\models\model_XGBoost.pkl')