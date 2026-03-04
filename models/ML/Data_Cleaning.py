import pandas as pd
import pickle
from pathlib import Path
data=pd.read_csv(r"Data\gym_members_exercise_tracking.csv")
pd.set_option('display.max_rows', 100)


def loging(info,mode='w'):
    with open("Data/Test.txt",f'{mode}') as f:
        f.write(f"{info}\n")
    print("Done")

def Outputing_rows(filename,filemode,output):
    filepath=Path("Data/Rows")
    if filepath.exists():
        pass
    else:
        filepath.mkdir(parents=True, exist_ok=True) 
    with open(f"{filepath}/{filename}.pkl",mode=filemode) as f:
        pickle.dump(output,f)



rename_map = {
    "Age": "Age",
    "Gender": "gender",
    "Weight (kg)": "weight",
    "Height (m)": "height",
    "Session_Duration (hours)": "Protien_Difference",
    "Workout_Frequency (days/week)": "Daysofweek",
    "BMI": "BMI"
}
data.rename(columns=rename_map, inplace=True)

SimilarColoums = [
    "Age", 
    "gender", 
    "weight", 
    "height", 
    "Protien_Difference", 
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
# for i in Final_Data:
#     loging(i.columns.tolist(),'a')
# print(Final_Data)
Outputing_rows(filename="Allrows",filemode='wb',output=alltherows)
for row in list(Final_Data.keys()):
    Outputing_rows(filename=row,filemode='wb',output=Final_Data[row])
