import os 
import xgboost as xgb
import numpy as np 


script_path = os.path.abspath(__file__)
current_dir = os.path.dirname(script_path)
requiredpath = os.path.join(current_dir, "Data")


Model=xgb.XGBRFRegressor()
Model.load_model(f"{current_dir}/Model.json")
sample_x = np.array([[25, 75.5, 1.75, 3, 24.6]])

#Index(['Age', 'weight', 'height', 'Daysofweek', 'BMI'], dtype='object')
def Predection(Age,weight,height,Daysofweek,BMI):
    sample_x=np.array([[Age,weight,height,Daysofweek,BMI]])
    values = Model.predict(sample_x)
    return values[0]


