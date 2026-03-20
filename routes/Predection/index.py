from flask import Blueprint,render_template,request,redirect,url_for,session
from .Functions.predictorvalue import fatpct
prd_bp=Blueprint('prd',__name__)


@prd_bp.route("/Predictor",methods=["POST","GET"])
def index():
    user_name = session.get('username')
    if request.method=="POST":
        return render_template("Predections/predictors.html",data=fatpct(username=user_name))
    
    return render_template("Predections/predictors.html",data=None)
    
