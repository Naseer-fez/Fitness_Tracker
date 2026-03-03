
import datetime
import calendar
try:
    from models.Calander_Table import Calander as cal
    from models.Sql_Tables import User
    from models.Sql_Tables import db
except ModuleNotFoundError as e:
    pass

notavailable='G'
Succues='S'
Notdone='N'
present='Y'
absent='R'
Fail="NO"

# now=datetime.now()
# date = now.day
# current_month_int = now.month
# current_year_int = now.year   
# weeks = calendar.monthcalendar(current_year_int, current_month_int)

def get_calendar_data():
    """Returns everything you need for the current moment."""
    now = datetime.datetime.now()
    return {
        "day": now.day,
        "month": now.month,
        "year": now.year,
        "weeks": calendar.monthcalendar(now.year, now.month),
        "full_now": now,
        "current_time":now.time()
    }


def transfer_to_db(userid,info,cal_data):
    if(isinstance(info,list)):
        output="".join(info)
    else:
        output=info

    trans=cal(user_id=userid,dates=output,month=cal_data['month'],
              Workoutdate=cal_data['full_now'].date(),time=cal_data['current_time']) 
    try:
        # db.session.add(trans)
        db.session.merge(trans)
        db.session.commit()
        return info
    except Exception as e:
        print(e)

        db.session.rollback()
       
        return Fail

def dates_maker(weeks,todaysdate,updates=0):
    # flattened = [day for week in weeks for day in week]
    if updates==0:
        flat_output = ""
        if updates ==0:
            for week in weeks:
                for day in week:
                    if day == todaysdate:
                        flat_output += present
                    elif day < todaysdate:
                        flat_output += notavailable
                    else:
                        flat_output += Notdone
        # print(flat_output)
        return flat_output



def get_today_index(todaysdate,weeks):
      inf=0
      for i in range(len(weeks)):

        for j in range(len(weeks[i])):

                if (todaysdate==weeks[i][j]):
                    inf=(i*7)+j
                    return inf

        
# def date_updates(week, todaysdate, status):
#     size = len(week)
#     output = [Notdone] * size
    
#     for i in range(size):
#         if i == todaysdate:
#             output[i] = status
#         elif week[i] == notavailable:
#             output[i] = notavailable
#         elif week[i] == present:
#             output[i] = present
#         elif week[i] == Succues:
#             output[i] = Succues

#     flag = []
#     for i in range(size):
#         if output[i] in (Succues, present):
#             flag.append(i)
            
#     for j in range(len(flag) - 1):
#         start = flag[j] + 1
#         end = flag[j + 1] 
        
#         for k in range(start, end):
#             if output[k] == Notdone:
#                 output[k] = absent

#     return output
        
            

def date_updates(week, todaysdate, status):
    size = len(week)
    
    output = [
        status if i == todaysdate
        else week[i] if week[i] in (notavailable, present, Succues)
        else Notdone
        for i in range(size)
    ]

    flags = [i for i, v in enumerate(output) if v in (Succues, present)]

    for start, end in zip(flags, flags[1:]):
        for k in range(start + 1, end):
            if output[k] == Notdone:
                output[k] = absent

    return output



           

                       

    




        
def data(user_name,update=0):
    cal_data=get_calendar_data()
    user=User.query.filter_by(username=user_name).first()
    if user is None:
        return "NO"
    id=user.id

    # date=12
    found_Cal=cal.query.filter_by(user_id=id).first()
    if found_Cal is None:
        info=dates_maker(weeks= cal_data['weeks'],todaysdate=cal_data['day'])
        transfer_to_db(userid=id,info=info,cal_data=cal_data)
        return info #the data is added into the db now , need to think about what if the data is nto added
    info=found_Cal.dates
    today_idx = get_today_index(todaysdate=cal_data['day'],weeks=cal_data['weeks'])
    elemnt=info[today_idx]
    if elemnt == notavailable or elemnt == Notdone:
        elemnt=present
    # print(elemnt)
    table_month=found_Cal.month
    send_mon=cal_data['month']
    flag=0
    if(table_month!=send_mon):
        info=dates_maker(weeks=cal_data['weeks'],todaysdate=cal_data['day'])
        transfer_to_db(userid=id,info=info,cal_data=cal_data)
        flag=1
        elemnt = info[today_idx]
    else:
        info=found_Cal.dates

       
            
    if update==0:
        output= date_updates(week=info,todaysdate=today_idx,status=elemnt)
        is_new_day = found_Cal.Workoutdate < cal_data['full_now'].date()
        if flag==1 or is_new_day:
            transfer_to_db(userid=id,info=output,cal_data=cal_data)


    else:
        output= date_updates(week=info,todaysdate=today_idx,status=Succues)
        transfer_to_db(userid=id,info=output,cal_data=cal_data)

    return output
    

    
if __name__=="__main__":
    # st= "GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGSNNNG"
    # print(len(st))
    now = datetime.datetime.now()
    print(now.date())
    print(now.time())
    pass
    # print(get_today_index(25))
    
    

   
    
    

#this is it

