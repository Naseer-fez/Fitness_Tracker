from functools import wraps
from flask import session, redirect, url_for, request, render_template
from Api_Rate.Enable import Access
import os

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'username' not in session:
            return redirect(url_for('auth.Login')) 
        return f(*args, **kwargs)
    return decorated_function




BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, 'Api_Rate', 'Data')

if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

def rate_limit(filena=None, allowedtime=50, freqattempts=10, attempts=10, required=1, filetype="json"):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            user_ip = request.remote_addr
            
            base_name = filena if filena else f.__name__
            full_path = os.path.join(DATA_DIR, f"{base_name}.{filetype}")
            
            result = Access(
                ip=user_ip, 
                allowedtime=allowedtime, 
                freqattempts=freqattempts,
                attempts=attempts, 
                required=required, 
                filetype=filetype, 
                filena=full_path
            )

            if result == 0:
                return render_template("Timeout.html")
            
            return f(*args, **kwargs)
        return decorated_function
    return decorator