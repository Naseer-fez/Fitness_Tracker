import pickle
from pathlib import Path
import os 
filepath=Path("Data/Rows")
def Fileoperation(filename,filemode='rb',destination=filepath,info=None):
    if filemode=='rb':
        with open(f"{destination}/{filename}.pkl",mode=filemode) as f:
            output=pickle.load(f)
            return output
    else:
         with open(f"{destination}/{filename}.pkl",mode=filemode) as f:
            pickle.dump(info,f)


def loging(info,mode='w'):
    with open("Data/Test.txt",f'{mode}') as f:
        f.write(f"{info}\n")
    print("Done")

# def findingfiles():
#     files=[]
#     for file in filepath.glob("*"):
#     #  print(f"Found file: {file.name}")
#         files.append(file.name)
#     print(files)
# print(Allrows)
# Allrows=Fileoperation(filename="Allrows")
Extradata=Fileoperation(filename="Extradata")
Heartdata=Fileoperation(filename="Heartdata")
Ml_data=Fileoperation(filename="Ml_data")
Similardata=Fileoperation(filename="Similardata")
