from models.Sql_Tables import User,Details
# from models.ML.Data_Cleaning import SimilarColoums
from models.ML.MLPredictor import Predection


SimilarColoums = [
    "Age", 
    "weight", 
    "height", 
    "Daysofweek", 
    "BMI"
]

def getthedb(user_name):
    user=User.query.filter_by(username=user_name).first()
    if user is None:
        return 0
    id=user.id
    details=Details.query.filter_by(user_id=id).first()
    if details is None:
        return -1
    # reqdata={}
    # for value in SimilarColoums:
    #     # reqdata.append(details.value)    
    #     reqdata[value]=getattr(details,value)
    reqdata = {col: getattr(details, col) for col in SimilarColoums}#optmizsed
    return reqdata





def fatpct(username):
    data=getthedb(user_name=username)
    if isinstance(data, dict):
        return Predection(**data)    
    return 0
    
    
