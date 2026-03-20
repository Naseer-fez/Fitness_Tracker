from flask import Blueprint,render_template,request
from .Functions import calculator as cal
# from Api_Rate.Api_Limiter import Api_Limit as ap
# limiter = ap()
# from Api_Rate.Enable import Access
from models.Decorators import rate_limit
Bmi_auth=Blueprint("BMI",__name__)


@Bmi_auth.route("/BmiCalculator",methods=["GET","POST"])
# @rate_limit()
def Bmi():

    
    return render_template("BMI/Bmi_Cal.html")


@Bmi_auth.route("/Calculator",methods=["GET","POST"])
# @rate_limit()
def calculator():


    if request.method=="POST":
        weight=request.form.get('weight')
        w_type=request.form.get('Kgs')
        height=request.form.get('Height')
        h_type=request.form.get('FT')
        values=cal.BMICalulator(weight,w_type,height,h_type)
        return render_template(
            "BMI/Cal_page.html",
            messages=values[0],
            Category=values[1]
        )