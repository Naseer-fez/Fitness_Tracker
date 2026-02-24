import yaml
from sklearn.linear_model import Ridge
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import pandas as pd

def load_schema(filename=r"DATA\DATA.yaml"):
    with open(filename, "r") as file:
        return yaml.safe_load(file)

def save_to_yaml(data, filename=r"DATA\Final_Data.yaml"):
    with open(filename, "w") as file:
        yaml.dump(data, file, default_flow_style=False)

schema = load_schema()

Heartdetails = schema["features"]["set_0"]
Data = schema["features"]["set_1"]
Fetures=Heartdetails+Data
heartdata=pd.read_csv(r"Data/Heart_details.csv")
maindata=pd.read_csv(r"Data/ML_Details.csv")
df=pd.concat([heartdata, maindata], axis=1)
target="Intensity_Score"

X=df[Fetures]
Y=df[target]


scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

model = Ridge(alpha=1.0)
model.fit(X_scaled, Y)

# Exporting parameters
slopes = dict(zip(Fetures, model.coef_.tolist()))
intercept = float(model.intercept_)

schema['linear_model'] = {
    'slopes': slopes,
    'intercept': intercept,
    'scaling_mean': dict(zip(Fetures, scaler.mean_.tolist())),
    'scaling_var': dict(zip(Fetures, scaler.var_.tolist()))
}

save_to_yaml(schema)
print("Data merged and coefficients saved to YAML.")
