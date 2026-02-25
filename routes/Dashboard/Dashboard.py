from flask import Blueprint,render_template,request,redirect,session
# from .Functions import Search_Db as search
# from Api_Rate.Api_Limiter import Api_Limit as ap

from Api_Rate.Enable import Access
from .Functions.Details import Entry
import threading
from models.Decorators import login_required,rate_limit
from models.Sql_Tables import User
from flask import current_app
from routes.Workout.Calander import data
from flask_login import current_user
dashboard_bp=Blueprint('dash',__name__)


# @dashboard_bp.before_request
# def check_access():
#     if Access(ip=request.remote_addr) == 0:
#         return render_template("Timeout.html")


@dashboard_bp.route("/DashBoard",methods=["POST","GET"])
@login_required
# @rate_limit()
def dashboard():
      user_name = session.get('username')
      if request.method=="POST":
            return render_template("Dashboard/Dashboard.html",messages=user_name,Data=data(user_name=user_name,update=1))
         
      return render_template("Dashboard/Dashboard.html",messages=user_name,Data=data(user_name=user_name,update=0))
        




@dashboard_bp.route("/Details",methods=["POST","GET"])
@login_required
# @rate_limit()
def details():
      fields = [
        "Age", "gender", "weight", "Weight_type", 
        "height", "Height_type", "Gym", "Protien", 
        "Protien_type", "Veg", "Daysofweek"
    ]
      if request.method=="POST":
           user_name=session['username']
           user = User.query.filter_by(username=user_name).first()
           user_data={key: request.form.get(key) for key in fields}
           user_data['user_id']=user.id
           app_instance = current_app._get_current_object()
           thread=thread = threading.Thread(target=Entry, args=( user_data,app_instance) )
           thread.start()
        
           return redirect("/DashBoard")

      return render_template("Dashboard/yourDetails.html")



@dashboard_bp.route("/Logout")
# @login_required
def Lofout():
      session.pop('username', None)
      return redirect("/Login")