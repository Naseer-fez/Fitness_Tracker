import pandas as pd
import yaml
data=pd.read_csv(r"Data\gym_members_exercise_tracking.csv")

def save_schema(cols_list, filename="schema.yaml"):
    schema = {
       "features": {f"set_{i}": list(cols) for i, cols in enumerate(cols_list)}
    }
    
    with open(filename, "w") as file:
        yaml.dump(schema, file)


# print(data.info())
d={"Male":"male","Female":"female"}
data['Gender'] = data['Gender'].map(d)


# print(data.info())
# 
data.columns = [c.replace('Workout_Frequency (days/week)', 'Daysofweek') for c in data.columns]
# data["Daysofweek"]=data["Workout_Frequency (days/week)"]
data=data.drop(columns=["Experience_Level","Water_Intake (liters)","Calories_Burned",
                        "Workout_Type","Session_Duration (hours)","Gender"],axis=1)

# print(data.info())
# print(data["Daysofweek"])
heartdetails = data[["Max_BPM","Avg_BPM","Resting_BPM","Age","Fat_Percentage"]].copy()
# print(heartdetails)

heartdetails['HR_Reserve'] = heartdetails['Max_BPM'] -heartdetails['Resting_BPM']
heartdetails['BPM_Range'] = heartdetails['Max_BPM'] - heartdetails['Avg_BPM']
heartdetails['Intensity_Score'] = (heartdetails['Avg_BPM'] / heartdetails['Max_BPM']) * 100

heartdetails.to_csv(r"Data\Heart_details.csv", index=False)
data.to_csv(r"Data\ML_Details.csv")

save_schema(cols_list=[heartdetails.columns,data.columns],filename=r"DATA\DATA.yaml")


