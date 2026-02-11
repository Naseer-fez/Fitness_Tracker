from flask import Flask
from routes.Login.Login import auth_bt 
from routes.CreateAccount.CreateAccount import Cre_acc
from models.Sql_Tables import db 
from routes.CreateAccount.Functions.Transdatato_Db import create_acc
from routes.BMI.Bmi_Cal import Bmi_auth
from Api_Limiter import Api_Limit as ap
from dotenv import load_dotenv
import os 
load_dotenv()

app = Flask(__name__)
Mysql_DB=os.getenv("Mysql_DB")
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://root:{Mysql_DB}@localhost/fitness_tracker'
db.init_app(app)
app.register_blueprint(create_acc)

app.register_blueprint(auth_bt)
app.register_blueprint(Cre_acc)
app.register_blueprint(Bmi_auth)

if __name__ == '__main__':
    with app.app_context():
        db.create_all() #this crrated the db if it is not created 
    app.run(debug=True)