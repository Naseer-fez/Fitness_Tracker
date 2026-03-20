from flask import Blueprint
from models.Sql_Tables import db,Details 

Dashboard_Details_Entry=Blueprint('create_account', __name__)



def dataEntry(app,userdata):
  with app.app_context():  
    try:
        Alreadeyexist=Details.query.get(userdata['user_id'])
        if Alreadeyexist:
             for key,value in userdata.items():
              if hasattr(Alreadeyexist, key):
                    setattr(Alreadeyexist,key,value)

        else:
            valid_cols = {k: v for k, v in userdata.items() if hasattr(Details, k)}
            data=Details(**valid_cols)
            db.session.add(data)
        db.session.commit()
        return True
    except Exception as e:
        db.session.rollback()
        with open("errors.txt", "a") as f:
                f.write(str(e) + "\n") 
        return False