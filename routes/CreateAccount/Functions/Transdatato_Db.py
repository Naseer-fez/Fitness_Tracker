from flask import Blueprint
from models.Sql_Tables import db,User
from .Hashing import hashdata
create_acc=Blueprint('create_account', __name__)
def inputdata(Username,Password):
        Username,Password=hashdata(username=Username,password=Password)
        data = User(username=Username, password=Password)
        try:
            db.session.add(data)
            db.session.commit()
        except Exception as e:
             return 0