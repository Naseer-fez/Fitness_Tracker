from .Api_Limiter import Api_Limit as ap 
from flask import request
import os 
import inspect
import json


Pre_ip=None
Pre_filena=None
Pre_allowedtime=20
Pre_freqattempts=5
Pre_attempts=5
Pre_required=1




def Access(ip=None,filena=None,allowedtime=20,freqattempts=5,attempts=5,required=1,filetype="json"):
    
    Pre_ip=ip
    Pre_allowedtime=allowedtime
    Pre_freqattempts=freqattempts
    Pre_attempts=attempts
    Pre_required=required
    Pre_filena=filena
    if filena ==None:
          Pre_filena=create_dynamic_file(type=filetype)
          __Fileopener(Pre_filena)

    limiter = ap(filename=Pre_filena)
    data = limiter.ratelimiter(ip=Pre_ip,filena=Pre_filena,allowedtime=Pre_allowedtime,
                                freqattempts=Pre_freqattempts,attempts=Pre_attempts,required=Pre_required)  
    if data != "Done":
            return 0
    else :
          return 1

def create_dynamic_file(type="json",filename=None):
        stack = inspect.stack()
        current_file = __file__
        caller_path = None

        for frame in stack:
            if frame.filename != current_file:
                caller_path = frame.filename
                break
        
        if caller_path:
            caller_name = os.path.splitext(os.path.basename(caller_path))[0]
            target_dir = os.path.join("Api_Rate", "Data")
            os.makedirs(target_dir, exist_ok=True)
            target_filename = os.path.join(target_dir, f"{caller_name}.{type}")
            return target_filename   
def __Fileopener(filena):
        filename=filena
        if(filena==None):
            filename=create_dynamic_file()
        try:  
            with open(filename, 'r') as file:
                    allips = json.load(file)
        except (FileNotFoundError,json.JSONDecodeError):
                allips={}
                with open(filename, 'w') as file:
                    json.dump(allips, file, indent=4)