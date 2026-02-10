from flask import Blueprint,render_template,request
from .Functions import calculator as cal
Bmi_auth=Blueprint("BMI",__name__)

@Bmi_auth.route("/BmiCalculator",methods=["GET","POST"])
def Bmi():
    return render_template("BMI/Bmi_Cal.html")


@Bmi_auth.route("/Calculator",methods=["GET","POST"])

def calculator():
    if request.method=="POST":
        weight=request.form.get('weight')
        w_type=request.form.get('Kgs')
        height=request.form.get('Height')
        h_type=request.form.get('FT')
        values=cal.BMICalulator(weight,w_type,height,h_type)
        return render_template(
            "BMI/Cal_page.html",
            messages=values
        )