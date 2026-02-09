from .import Transdatato_Db as db

def verify(username,password,rename,repass):
    
    if username!=rename:
        return [0,"Enter the Username"]
    if repass!=password:
        return   [0,"Password Dont match"]
    value=db.inputdata(username,password)
    if(value==0):
        return [0,"Username Already exist"]
    return [1,1]

    