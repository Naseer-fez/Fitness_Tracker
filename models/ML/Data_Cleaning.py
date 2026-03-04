import pandas as pd
import pickle
from pathlib import Path
import os 
currentdir=os.getcwd()
requiredpath=os.path.join(currentdir,r"Data\Gymdata")


def concatdata():
    folder=requiredpath
    dataframes_list = []
    for file  in os.listdir(folder):
        if file.endswith(".csv"):
            full_file_path = os.path.join(folder, file)
            temp_df = pd.read_csv(full_file_path)
            dataframes_list.append(temp_df)
        if dataframes_list:
            Final_Data=pd.concat(dataframes_list,ignore_index=True)
            return Final_Data
        else:
            return pd.DataFrame()

data=concatdata()


def loging(info,mode='w'):
    with open("Data/Test.txt",f'{mode}') as f:
        f.write(f"{info}\n")
    print("Done")

def Outputing_rows(filename,filemode,output):
    filepath=Path(os.path.join(currentdir,"Data"))
    filepath.mkdir(parents=True, exist_ok=True)
    with open(f"{filepath}/{filename}.pkl",mode=filemode) as f:
        pickle.dump(output,f)

def outputing_csv(filename,output):
        filepath=Path(os.path.join(currentdir,"Data/ML_Data"))
        filepath.mkdir(parents=True, exist_ok=True)

        output.to_csv(f"{filepath}/{filename}.csv",index=False)
        

rename_map = {
    "Age": "Age",
    "Gender": "gender",
    "Weight (kg)": "weight",
    "Height (m)": "height",
    # "Session_Duration (hours)": "Protien_Difference",
    "Workout_Frequency (days/week)": "Daysofweek",
    "BMI": "BMI"
}
data.rename(columns=rename_map, inplace=True)

SimilarColoums = [
    "Age", 
    "weight", 
    "height", 
    "Daysofweek", 
    "BMI"
]

Heartrealted=[ 
"Max_BPM",
"Avg_BPM",
"Resting_BPM"]
drop=[
"Calories_Burned",
"Workout_Type",
"Water_Intake (liters)",
"Experience_Level"]
important=[
    "Fat_Percentage",
    "Experience_Level"
]

# Similar=data.drop(columns=((Heartrealted)),inplace=False)
Similardata=data[SimilarColoums]
Heartdata=data[Heartrealted]
Extradata=data[drop]
Ml_Data=data[important]

alltherows=["Similardata","Heartdata","Extradata","Ml_Data"]

Final_Data = {name: locals()[name] for name in alltherows}

# Outputing_rows(filename="Allrows",filemode='wb',output=alltherows)

for row in list(Final_Data.keys()):
    outputing_csv(filename=row,output=Final_Data[row])

# loging(Similardata.dtypes)