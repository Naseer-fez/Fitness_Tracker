from models.Chatbot.Ai_Model import Chatbot
from flask import Blueprint,render_template,request

Cht_bp=Blueprint("Cht",__name__)

#def Chatbot(UserPromt,AiModels=None,SystemPromt=SystPromt):
@Cht_bp.route("/Chat",methods=['GET', 'POST'])
def Fun():
    if  request.method=="POST":
        promt=request.form.get("Promt")
        return render_template("Chatbot/index.html",Data=Chatbot(user_promt=promt))
    return render_template("Chatbot/index.html")
 



    pass