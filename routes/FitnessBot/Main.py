from models.Chatbot.Ai_Model import Chatbot
from flask import Blueprint,render_template,request
from models.Decorators import login_required
Cht_bp=Blueprint("Cht",__name__)

#def Chatbot(UserPromt,AiModels=None,SystemPromt=SystPromt):
@Cht_bp.route("/Chat",methods=['GET', 'POST'])
@login_required
def Fun():
    if  request.method=="POST":
        promt=request.form.get("Promt")
        # print("HII")
        return render_template("Chatbot/index.html",Data=Chatbot(UserPromt=promt))
    # print("HIIIIIIII")
    return render_template("Chatbot/index.html")



    pass