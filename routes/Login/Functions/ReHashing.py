import ctypes as C
import os 
import platform
def systemversion():
    system=platform.system()
    if system=="Windows":
        return "dll"
    elif system=="Linus":
        return "so"
    else:
        raise Exception("Os not found")

curentpath=os.path.dirname(os.path.abspath(__file__))

def rehashdata(username,password,hashedpassword):
    filetype=systemversion()
    hash=C.CDLL(os.path.join(curentpath,f"Rehash.{filetype}"))
    reshah=hash.Rehash
    reshah.argtypes=[C.c_char_p,C.c_char_p,C.c_char_p]
    reshah.restype=C.c_int
    encuser=username.encode()
    encpas=password.encode()
    if isinstance(hashedpassword, bytes):
        enchash = hashedpassword
    else:
        enchash = hashedpassword.encode('utf-8')
    checking=reshah(encuser,encpas,enchash)
    if  checking==1:
        return 1
    else:
        return 0

    
