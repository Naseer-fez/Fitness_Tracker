from flask import Blueprint,render_template,request,redirect,session
from .Functions import Search_Db as search
# from Api_Rate.Api_Limiter import Api_Limit as ap
from Api_Rate.Enable import Access
auth_bt=Blueprint('auth',__name__)
from models.Decorators import rate_limit

# limiter = ap()


@auth_bt.route("/Login",methods=['GET', 'POST'])
@rate_limit(allowedtime=40,freqattempts=10,attempts=20)
def Login():
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
        value=search.checking_password(username,password)
        if(value[0]):
            session['username']=username
            return redirect("/DashBoard")
        else:
            return render_template("login.html",messages=value[1])


    return render_template("login.html")



