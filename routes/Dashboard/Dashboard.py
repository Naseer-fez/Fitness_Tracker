from flask import Blueprint,render_template,request,redirect,session
# from .Functions import Search_Db as search
# from Api_Rate.Api_Limiter import Api_Limit as ap
from Api_Rate.Enable import Access
from .Functions.Details import Entry
import threading
from models.Decorators import login_required,rate_limit
dashboard_bp=Blueprint('dash',__name__)


# @dashboard_bp.before_request
# def check_access():
#     if Access(ip=request.remote_addr) == 0:
#         return render_template("Timeout.html")


@dashboard_bp.route("/DashBoard",methods=["POST","GET"])
@login_required
@rate_limit()
def dashboard():

         user_name=session['username']
         return render_template("Dashboard/Dashboard.html",messages=user_name)
        




@dashboard_bp.route("/Details",methods=["POST","GET"])
@login_required
# @rate_limit()
def details():
      fields = [ "Age", "gender", "weight", "kgs", "Height", 
    "FT", "Gym", "Protein", "prot_unit", "veg", "noofdays"]
      if request.method=="POST":
           user_data={key: request.form.get(key) for key in fields}
           thread=threading.Thread(target=Entry,args=(user_data,fields))
           thread.start()
        
           return redirect("/DashBoard")

      return render_template("Dashboard/yourDetails.html")



@dashboard_bp.route("/Logout")
# @login_required
def Lofout():
      session.pop('username', None)
      return redirect("/Login")