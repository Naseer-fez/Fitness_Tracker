from flask import Blueprint,render_template,request,redirect,url_for
from .Functions import  verfication as vy
# from Api_Rate.Api_Limiter import Api_Limit as ap 
from Api_Rate.Enable import Access
from models.Decorators import rate_limit
Cre_acc=Blueprint('CRC',__name__)

# limiter = ap()


@Cre_acc.route("/Create",methods=["POST","GET"])
@rate_limit()
def Creation_Account():
    # userip = request.remote_addr
    # data = limiter.ratelimiter(ip=userip,filena=None,allowedtime=20,
    #                            freqattempts=5,attempts=5,required=1)   
    # if data != "Done":
    #     return f"Too Many Attempts wait for {data} secs \n "
    if Access(ip=request.remote_addr)==0:
        return render_template("Timeout.html")
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
        
