from models.Sql_Tables import db
from models.Calander_Table import Calander as cal
from datetime import datetime,timedelta
from app import app
from sqlalchemy.orm import Session
now=datetime.now()
# todays_date = now.day
# present_time=now.time()
# yesterday = todays_date - timedelta(days=1)
# senderemail="sknaseer.fez@gmail.com"
# threshold = datetime.now() - timedelta(hours=24)

email="sknaseer.fez@gmail.com"
allowedtime=24
allowedday=1

def changefactors(sender_email=None, timelimit=None, days=None):
    global email, allowedtime, allowedday
    if sender_email: email = sender_email
    if timelimit: timelimit = allowedtime
    if days: allowedday = days
    
time_data = {
    "todays_date": now.date(),                     
    "present_time": now.time(),                     
    "yesterday": (now - timedelta(days=allowedday )).date(),   
    "threshold": now - timedelta(hours=allowedtime),          
    "sender_email": email
}


def Messages_to_send(to,msg_info=1,date=None,frm=time_data["senderemail"]):
    to=to.split('@')[0]
    frm=frm.split('@')[0]

    date = date or "Not Available"
    if msg_info==1:
        promt="""
        Dear {to},
        This has been Noticed that you have missed Today's({Date}) workout,
        This is a seriouly action we would like you to remind this so that u will work 
        double the action which u do today .
        
        your regards,
        Team {frm}.        
        """
        
    return email_sender(to=to,frm=frm)

def Email_extractor(timelimit=time_data["threshold"]):
    while True:
        with   app.app_context():
            records=cal.query.filter( ((cal.time < timelimit ))).all()
            for record in records:
                userid=record.user_id
                verifincarion=Messages_to_send(to=userid,date=time_data["yesterday"],frm=time_data["sender_email"],msg_info=1)
                if verifincarion==0:
                    raise TypeError("Email Sending failed")# or create a log of this 
                
                
def email_sender(to,frm=time_data["sender_email"]):
        return 1
        #need to write the real code here
    

            
                
    
