import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder 
from sklearn.pipeline import Pipeline, FeatureUnion
from sklearn_features.transformers import DataFrameSelector



FILE_PATH = "data\WA_Fn-UseC_-Telco-Customer-Churn.csv"
df = pd.read_csv(FILE_PATH)

df.drop(columns=['customerID'], axis=1, inplace=True)
df['TotalCharges'] = pd.to_numeric(df.TotalCharges, errors='coerce')
df.dropna(inplace=True)

df["SeniorCitizen"] = df["SeniorCitizen"].replace({1: "Yes", 0: "No"})

X = df.drop(columns=['Churn'], axis=1)
y = df['Churn'].apply(lambda x: 1 if x == 'Yes' else 0)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

num_cols = [col for col in X_train.columns if X_train[col].dtype in ['float32', 'float64', 'int32', 'int64']]
categ_cols = [col for col in X_train.columns if X_train[col].dtype not in ['float32', 'float64', 'int32', 'int64']]



num_pipeline = Pipeline([
                        ('selector', DataFrameSelector(num_cols)),   
                        ('scaler', StandardScaler())
                        ])


categ_pipeline = Pipeline(steps=[
            ('selector', DataFrameSelector(categ_cols)),    
            ('OHE', OneHotEncoder(sparse_output=False))])

total_pipeline = FeatureUnion(transformer_list=[
                                            ('num_pipe', num_pipeline),
                                            ('categ_pipe', categ_pipeline)
                                               ]
                             )
X_train_final = total_pipeline.fit_transform(X_train)
X_test_final = total_pipeline.transform(X_test)  

def preprocess_new(X_new):
 
    return total_pipeline.transform(X_new)           
 
