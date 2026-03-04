import pickle 
import os 
import pandas as pd
import xgboost as xgb
currentdir=os.getcwd()
requiredpath=os.path.join(currentdir,"Data/ML_data")


similardata=pd.read_csv(f"{requiredpath}/Similardata.csv")

MLdata=pd.read_csv(f"{requiredpath}/Ml_Data.csv")
mlrows=MLdata.columns

# heartdata=pd.read_csv(f"{requiredpath}/Heartdata.csv")
# Extradata=pd.read_csv(f"{requiredpath}/Extradata.csv")

X=similardata

Y=MLdata[mlrows[0]]
# print(X.columns)
# print(similardata.dtypes)
# print(Y.dtype)


Model = xgb.XGBRegressor(
    n_estimators=500,   
    max_depth=3,         
    learning_rate=0.05, 
    reg_lambda=10,     
    subsample=0.8,      
    colsample_bytree=0.8 
)
Model.fit(X,Y)
Model.save_model(f"{currentdir}/Model.json")
# def averageerror():
    # from sklearn.model_selection import cross_val_score
    # scores = cross_val_score(Model, X, Y, scoring='neg_mean_squared_error', cv=5)
    # print(f"Average Error: {np.sqrt(-scores.mean())}")
