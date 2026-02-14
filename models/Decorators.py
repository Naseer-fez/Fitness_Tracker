from functools import wraps
from flask import session, redirect, url_for, request, render_template
from Api_Rate.Enable import Access

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'username' not in session:
            return redirect(url_for('auth.Login'))
        return f(*args, **kwargs)
    return decorated_function

def rate_limit(allowedtime=50, freqattempts=10, attempts=10, required=1, filetype="json"):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            user_ip = request.remote_addr
            
            # This captures 'DashBoard', 'home', etc. 
            # It ensures the 'Access' function treats each route as a unique key.
            target_key = f.__name__
            
            result = Access(
                ip=user_ip, 
                allowedtime=allowedtime, 
                freqattempts=freqattempts,
                attempts=attempts, 
                required=required, 
                filetype=filetype, 
                filena=target_key 
            )

            if result == 0:
                return render_template("Timeout.html")
            
            return f(*args, **kwargs)
        return decorated_function
    return decorator