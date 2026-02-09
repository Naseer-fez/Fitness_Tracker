from flask import Blueprint,render_template,request
# import password_check 

auth_bt=Blueprint('auth',__name__)

@auth_bt.route("/Login",methods=['GET', 'POST'])
def Login():
    if request.method=="POST":
        username=request.form.get('username')
    password=request.form.get('Password')

    return render_template("login.html")



