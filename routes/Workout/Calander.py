
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



def transfer_to_db(userid,info):
    if(isinstance(info,list)):
        output="".join(info)
    else:
        output=info
    trans=cal(user_id=userid,dates=output)
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

# def get_today_index(weeks, todaysdate):
#     today_int = todaysdate.day if hasattr(todaysdate, 'day') else int(todaysdate)
#     count = 0
#     for i, cell in enumerate(weeks):
#         if cell != notavailable:  # Skip 'G' (padding), count everything else
#             count += 1
#             if count == today_int:
#                 return i
#     return -1

def get_today_index(weeks, todaysdate):
    
    now = datetime.now()
    cal_grid = calendar.monthcalendar(now.year, now.month)
    flat_cal = [day for week in cal_grid for day in week]
    today_int = todaysdate.day if hasattr(todaysdate, 'day') else int(todaysdate)
    
    for i, day_number in enumerate(flat_cal):
        if day_number == today_int:
            return i
            
    return -1  # No comma



def date_updates(weeks,todaysdate,status):
        size=len(weeks)
        flag=[]
        output=[Notdone]*(size)
        # print(get_today_index(weeks=weeks,todaysdate=todaysdate))
        today_idx = get_today_index(weeks=weeks, todaysdate=todaysdate)

        # todaysdate=get_today_index(weeks=weeks,todaysdate=todaysdate)
        output[today_idx]=status
        # print(weeks)
        for i in range(size):
            # if i == todaysdate:
            #     continue
            if weeks[i]==notavailable:
                output[i]=notavailable
            if weeks[i]==present:
                output[i]=present      
            if ((weeks[i]==Succues)):
                output[i]=Succues
                flag.append(i+1)
            if ( (output[i]==Succues)or(output[i]==present)):
                flag.append(i+1)
                print(flag)
        
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
    now=datetime.now()

    date = now.day
    # date=12
    found_Cal=cal.query.filter_by(user_id=id).first()
    if found_Cal is None:
        current_month_int = now.month
        current_year_int = now.year   
        weeks = calendar.monthcalendar(current_year_int, current_month_int)
        info=dates_maker(weeks=weeks,todaysdate=date)
        transfer_to_db(userid=id,info=info)
        return info #the data is added into the db now , need to think about what if the data is nto added
    info=found_Cal.dates
    # if update==0:
    #     return info
    # #Now for update dates
    # # print(test)
    if update==0:
        output= date_updates(weeks=info,todaysdate=date,status=present)
        return output
    else:
        
        # if info[today_idx] == Succues:
        #     return info
        output= date_updates(weeks=info,todaysdate=date,status=Succues)
        transfer_to_db(userid=id,info=output)
                # print(output)
        return output
    

    
if __name__=="__main__":
    st= "GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGSNNNG"
    print(len(st))
    test=[]
    for i in st:
        test.append(i)
    # print(get_today_index(weeks=weeks,todaysdate=26))
    # print(weeks[get_today_index(weeks=weeks,todaysdate=26)])
    print(date_updates(weeks=test,todaysdate=26))
    
    
    
    
    

#this is it

