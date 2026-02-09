from flask import Flask
from routes.Login.Login import auth_bt  # Import the blueprint variable
from routes.CreateAccount.CreateAccount import Cre_acc
from models.Sql_Achmy import db  # Import the hub
from routes.CreateAccount.Functions.Transdatato_Db import create_acc


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db.init_app(app)
app.register_blueprint(create_acc)

# app.register_blueprint(auth_bt)
app.register_blueprint(Cre_acc)
# ... (your imports and config)

# ... (your db.init_app(app) line)

if __name__ == '__main__':
    with app.app_context():
        # THIS LINE IS CRITICAL: It creates the 'users.db' file and the 'user' table!
        db.create_all() 
    app.run(debug=True)