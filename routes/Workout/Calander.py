import calendar
from datetime import datetime

current_month_int = datetime.now().month
current_year_int = datetime.now().year

weeks = calendar.monthcalendar(current_year_int, current_month_int)

# for week in weeks:
#     print(week)
# print(weeks)
# grey is no dayy , p is green means presnt , a means , red
see = []

for week in weeks:
    row = []
    for day in week:
        if day == 0:
            row.append("G")  
        elif day == 1:       
            row.append("A") 
        else:
            row.append("P")  
    see.append(row)
print(see)  

def data():
    return see