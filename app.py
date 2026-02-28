from flask import Flask
# from flask import request,render_template
# from Api_Rate.Enable import Access
from routes.Login.Login import auth_bt 
from routes.CreateAccount.CreateAccount import Cre_acc
from models.Sql_Tables import db 
from routes.CreateAccount.Functions.Transdatato_Db import create_acc
from routes.BMI.Bmi_Cal import Bmi_auth
from routes.Dashboard.Dashboard import dashboard_bp
from routes.Welcome.hello import Hi_bp
from routes.Dashboard.Functions.Dataentry import Dashboard_Details_Entry

# from models.Calander_Table import db
# from models.Calander_Table import Calander
# db.create_all()
from dotenv import load_dotenv
import os 
load_dotenv()

app = Flask(__name__)
Mysql_DB=os.getenv("Mysql_DB")
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://root:{Mysql_DB}@localhost/fitness_tracker'
app.secret_key=os.getenv("SECRET_KEY")
db.init_app(app)

app.register_blueprint(create_acc)
app.register_blueprint(dashboard_bp)
app.register_blueprint(auth_bt)
app.register_blueprint(Cre_acc)
app.register_blueprint(Bmi_auth)
app.register_blueprint(Hi_bp)
# app.register_blueprint(Dashboard_Details_Entry)
# @app.before_request
# def check_access():
#     # This will run before every single request to your server
#     if Access(ip=request.remote_addr) == 0:
#         return render_template("Timeout.html")

if __name__ == '__main__':
    with app.app_context():
        db.create_all() #this crrated the db if it is not created 
    app.run(debug=True)