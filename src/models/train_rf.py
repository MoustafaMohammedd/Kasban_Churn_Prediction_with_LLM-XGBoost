import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from src.utils.data_preprocessing_pipeline import X_train_final, y_train
import numpy as np 
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import RandomizedSearchCV, cross_val_score
import joblib

rf_model = RandomForestClassifier(random_state=42)

params_best_forest = {'n_estimators': np.arange(100, 500, 50), 
                      'max_depth': np.arange(4, 20, 2), 
                      'max_samples': [0.7, 0.8, 0.9, 1]}

search_random_forest = RandomizedSearchCV( estimator=rf_model, param_distributions=params_best_forest, 
                                          n_iter=20, scoring="f1_weighted", 
                                          cv=5, verbose=6, random_state=42)
search_random_forest.fit(X_train_final, y_train)


best_foresr_params = search_random_forest.best_params_
print('best_foresr_params -- ', best_foresr_params)

best_forest = search_random_forest.best_estimator_  
print('best_forest -- ', best_forest)

f1_scores_tuned_forest = cross_val_score(estimator=best_forest, X=X_train_final, y=y_train, 
                               cv=5, scoring='f1_weighted', n_jobs=-1)  

print(f'Scores Using Tuned RandomForest --- {np.round(f1_scores_tuned_forest, 4)}')
print(f'Mean Scores Using Tuned RandomForest --- {f1_scores_tuned_forest.mean():.4f}')


joblib.dump(best_forest, 'src\models\model_RF2.pkl')