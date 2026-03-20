from flask import render_template,Blueprint,request
# from flask.blueprints import Blueprint
from Api_Rate.Enable import Access
Hi_bp=Blueprint('hii',__name__)


@Hi_bp.route("/")
def hi():
    if Access(ip=request.remote_addr,freqattempts=40)==0:
        return render_template("Timeout.html")
    return render_template("Welcome.html")

