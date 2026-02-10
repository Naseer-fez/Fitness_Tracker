from flask import Blueprint,render_template,request,redirect
# import password_check 
from .Functions import Search_Db as search
auth_bt=Blueprint('auth',__name__)

@auth_bt.route("/Login",methods=['GET', 'POST'])
def Login():
    if request.method=="POST":
        username=request.form.get('username')
        password=request.form.get('Password')
        value=search.checking_password(username,password)
        if(value[0]):
            return redirect("/BmiCalculator")
        else:
            return render_template("login.html",messages=value[1])


    return render_template("login.html")



