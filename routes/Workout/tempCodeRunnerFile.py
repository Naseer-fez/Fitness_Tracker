from datetime import datetime, timedelta


past_time = datetime.now() - timedelta(hours=24.000001)


now = datetime.now()


difference = now - past_time

if difference > timedelta(hours=24):
    print("More than 24 hours have passed!")
else:
    print("It has been less than 24 hours.")