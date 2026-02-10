from flask import Blueprint,render_template,request,redirect,url_for
from .Functions import  verfication as vy

Cre_acc=Blueprint('CRC',__name__)
@Cre_acc.route("/Create",methods=["POST","GET"])
def Creation_Account():
    if request.method=="POST":
        username=request.form.get('username')
        password=request.form.get('Password')
        # rename=request.form.get('rename')
        repass=request.form.get('repass')
        msg=vy.verify(username,password,repass)
        if (msg[0]==0):
            return render_template("CreateAccount.html",messages=msg[1])
        else:
            return redirect("/Login")
    return render_template("CreateAccount.html")
        
