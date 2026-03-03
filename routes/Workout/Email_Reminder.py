from models.Sql_Tables import db
from models.Calander_Table import Calander as cal
from datetime import datetime,timedelta
from flask import Blueprint,current_app
from models.Sql_Tables import User
from dotenv import load_dotenv
import os
from email.message import EmailMessage
import smtplib as smpt
import ssl
import time
import threading


Reminder_app=Blueprint("Reminder",__name__)

load_dotenv()
now=datetime.now()
email=os.getenv("Email")
password=os.getenv("Email_password")
allowedtime=24
allowedday=1

def changefactors(sender_email=None, timelimit=None, days=None):
    global email, allowedtime, allowedday
    if sender_email: email = sender_email
    if timelimit: allowedtime=timelimit
    if days: allowedday = days
    
time_data = {
    "todays_date": now.date(),                     
    "present_time": now.time(),                     
    "yesterday": (now - timedelta(days=allowedday )).date(),   
    "threshold": now - timedelta(hours=allowedtime),          
    "sender_email": email
}

def log_result(status,email=None,log_type=1):
    if log_type==1:
        with open("mail_log.txt", "a") as f:
            f.write(f"{datetime.now()} - {email} - {status}\n")
    elif log_type==2:
        with open("Db_ERROR.txt",'a') as f:
            f.write(f"{datetime.now().time()}-->{status}\n")
    else:
            with open("General_ERROR.txt",'a') as f:
                f.write(f"{datetime.now().time()}-->{status}\n")

def Messages_to_send(to,msg_info=1,date=None,frm=time_data["sender_email"]):
    receiver = f"{to}@gmail.com" if "@" not in to else to
    # receiver=to
    # sender=frm.partition('@')[0]
    date = date or "Not Available"
    if msg_info==1:
        content=f"""Hey You --> {to.partition('@')[0]},Arent you gonna workout today ???"""
        
    msg=EmailMessage()
    msg["Subject"]="You Have missed You Workout Today"
    msg["To"]=receiver
    msg["From"]=frm
    msg.set_content(content)
    return email_sender(to=to,frm=frm,Message=msg)



def Email_extractor(app,timelimit=None):

    global email, allowedtime, allowedday
    while True:
        with   app.app_context():
            # log_result(log_type=33, status="Step 1: Background Loop Started")
            current_now = datetime.now()
            current_threshold = current_now - timedelta(hours=allowedtime)
            today_date = current_now.date()
            records=cal.query.filter( ((cal.time < current_threshold ))).all()
            yesterday_date = (current_now - timedelta(days=allowedday)).date()
            for record in records:
                userid=record.user_id
                Username=User.query.filter_by(id=userid).first()
                Username=Username.username
                Verification=Messages_to_send(to=Username,date=yesterday_date,frm=time_data["sender_email"],msg_info=1)
                if Verification==0:
                    log_result(status=f"Failed to send to {userid}", log_type=1)
                    continue
                else:
                    record.Workoutdate=today_date
                    record.time=datetime.now()
            try:
                db.session.commit()
            except Exception as e:
                    db.session.rollback()
                    log_result(status=e,log_type=0)
               
        time.sleep(10)
                
                
def email_sender(to,Message,frm=time_data["sender_email"]):
        cont=ssl.create_default_context()
        GMAIL_SERVER = "smtp.gmail.com"
        try:
            with smpt.SMTP_SSL(host=GMAIL_SERVER,port=465,context=cont) as server:
                server.login(email,password)
                server.send_message(Message)
                return 1
        except Exception as e:
            print(f"The error is {e}")
            log_result(email=to,status=e)
            return 0
    

def EmailReminder(sender_email=email, timelimit=10, days=1):
    changefactors(sender_email=sender_email,timelimit=timelimit,days=days)
    actual_app = current_app._get_current_object()
    try:
        thread=threading.Thread(target=Email_extractor,args=(actual_app,timelimit,))
        thread.daemon=True
        thread.start()
        # log_result(log_type=33, status="SYSTEM: Thread Started Successfully")
    except Exception as e:
        log_result(log_type=0, status=f"Thread Launch Failed: {e}")
                
    
