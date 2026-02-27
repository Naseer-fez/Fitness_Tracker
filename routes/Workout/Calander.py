
import calendar
from datetime import datetime
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

now=datetime.now()
date = now.day
current_month_int = now.month
current_year_int = now.year   
weeks = calendar.monthcalendar(current_year_int, current_month_int)

def transfer_to_db(userid,info,des_mon=current_month_int):
    if(isinstance(info,list)):
        output="".join(info)
    else:
        output=info
    
    trans=cal(user_id=userid,dates=output,month=des_mon,date=now.date(),time=now.time())
    try:
        # db.session.add(trans)
        db.session.merge(trans)
        db.session.commit()
        return info
    except Exception as e:
        print(e)

        db.session.rollback()
       
        return Fail

def dates_maker(week,todaysdate,updates=0):
    # flattened = [day for week in weeks for day in week]
    if updates==0:
        flat_output = ""
        if updates ==0:
            for week in week:
                for day in week:
                    if day == todaysdate:
                        flat_output += present
                    elif day < todaysdate:
                        flat_output += notavailable
                    else:
                        flat_output += Notdone
        # print(flat_output)
        return flat_output

# def get_today_index(weeks, todaysdate):
#     today_int = todaysdate.day if hasattr(todaysdate, 'day') else int(todaysdate)
#     count = 0
#     for i, cell in enumerate(weeks):
#         if cell != notavailable:  # Skip 'G' (padding), count everything else
#             count += 1
#             if count == today_int:
#                 return i
#     return -1

def get_today_index(todaysdate):
      inf=0
      for i in range(len(weeks)):

        for j in range(len(weeks[i])):

                if (todaysdate==weeks[i][j]):
                    inf=(i*7)+j
                    return inf

        
        
            




def date_updates(week,todaysdate,status):
        size=len(week)
        flag=[]
        output=[Notdone]*(size)
        # print(get_today_index(weeks=weeks,todaysdate=todaysdate))
        

        # todaysdate=get_today_index(weeks=weeks,todaysdate=todaysdate)
        output[todaysdate]=status
        # print(weeks)
        for i in range(size):
            if i == todaysdate:
                continue
            if week[i]==notavailable:
                output[i]=notavailable
            if (week[i]==present):
                output[i]=present      
            if ((week[i]==Succues)):
                output[i]=Succues
                flag.append(i+1)
            if ( (output[i]==Succues)or(output[i]==present)):
                flag.append(i+1)

        
            for j in range(len(flag)-1):
                    # output[flag[j]:flag[j+1]-1]=absent  
                    start = flag[j]
                    end = flag[j + 1]-1
                    # print((start,end))
                    output[start:end] = [absent] * (end - start)                

        # print(output)                       
        return output
    

           

                       

    




        
def data(user_name,update=0):
    user=User.query.filter_by(username=user_name).first()
    if user is None:
        return Fail
    id=user.id

    # date=12
    found_Cal=cal.query.filter_by(user_id=id).first()
    if found_Cal is None:
        info=dates_maker(week=weeks,todaysdate=date)
        transfer_to_db(userid=id,info=info,des_mon=current_month_int)
        return info #the data is added into the db now , need to think about what if the data is nto added
    info=found_Cal.dates
    today_idx = get_today_index(todaysdate=date)
    elemnt=info[today_idx]
    if elemnt==notavailable:
        elemnt=present
    # print(elemnt)
    table_month=found_Cal.month
    send_mon=current_month_int
    flag=0
    if(table_month!=send_mon):
        info=dates_maker(week=weeks,todaysdate=date)
        transfer_to_db(userid=id,info=info,des_mon=current_month_int)
        flag=1
        elemnt = info[today_idx]
    else:
        info=found_Cal.dates

       
            
    if update==0:
        output= date_updates(week=info,todaysdate=today_idx,status=elemnt)
        if flag==1:
            transfer_to_db(userid=id,info=output,des_mon=send_mon)

        return output
    else:
        output= date_updates(week=info,todaysdate=today_idx,status=Succues)
        transfer_to_db(userid=id,info=output,des_mon=send_mon)

        return output
    

    
if __name__=="__main__":
    # st= "GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGSNNNG"
    # print(len(st))
    print(now.date())
    print(now.time())
    pass
    # print(get_today_index(25))
    
    

   
    
    

#this is it

