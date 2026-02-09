from .import Transdatato_Db as db

def verify(username,password,rename,repass):
    
    if username!=rename:
        return [0,"Enter the Username"]
    if repass!=password:
        return   [0,"Password Dont match"]
    db.inputdata(username,password)
    return [1,1]

    