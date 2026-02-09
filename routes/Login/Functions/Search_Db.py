from models.Sql_Tables import User

def checking_password(username1,password):
        found_user=User.query.filter_by(username=username1).first()
        if(found_user):
                stored_password = found_user.password
                if(stored_password==password):
                        return [1]
                return [0,"Wrong Password"]
        return [0,f"Username :{username1} Not Found"]
