import calendar
from datetime import datetime
from models.Calander_Table import Calander as cal
from models.Sql_Tables import User

def transfer_to_db(username,dates):
    user = User.query.filter_by(username=username).first()
    userid=user.id
    trans=cal(userid,dates)
    try:
        cal.session.add(trans)
        cal.commit(trans)
    except Exception as e:
        return "NO"
    
    
    
    pass

def dates_maker(weeks,todaysdate,updates=0):
    # flattened = [day for week in weeks for day in week]
    flat_output = ""
    if updates ==0:
        for week in weeks:
            for day in week:
                if day == todaysdate:
                    flat_output += "Y"
                elif day < todaysdate:
                    flat_output += "G"
                else:
                    flat_output += "B"
    

    return flat_output
                

    
    


def data(username1,update=None):
    user = User.query.filter_by(username=username1).first()
    user_idx = user.id
    try:
        found_user=User.query.filter_by(user_id=user_idx).first()
    except Exception as e:
        print(e)
        return "Y"
    if(found_user is not None):
        data=cal.dates
    else:
        data=1
        
        
    
    if(data is None):
        now=datetime.now()
        current_month_int = now.month
        current_year_int = now.year
        today_date = now.day
        weeks = calendar.monthcalendar(current_year_int, current_month_int)
        info=dates_maker(weeks=weeks,todaysdate=today_date,updates=0)
        
    else :
        info= found_user.dates
        if(update):
            now=datetime.now()
            today_date = now.day
            today_index = info.index(today_date)
            info[today_index]='S'
            info=dates_maker()
    check=transfer_to_db(username=username1,dates=info)
    if check=="NO":
        return "NO"           
        
        
    return info

        
    


    # return dates

now=datetime.now()
current_month_int = now.month
current_year_int = now.year
today_date = now.day
weeks = calendar.monthcalendar(current_year_int, current_month_int)
dates_maker(weeks=weeks,todaysdate=today_date)

