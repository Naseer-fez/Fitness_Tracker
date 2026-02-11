import ctypes as C
import os 
curentpath=os.path.dirname(os.path.abspath(__file__))

def hashdata(username,password):
    hash=C.CDLL(os.path.join(curentpath,"Hashfun.dll"))
    hashfun=hash.Hashreturn
    hashfun.argtypes=[C.c_char_p,C.c_char_p]
    hashfun.restype=C.c_char_p
    encuser=username.encode('utf-8')
    encpas=password.encode('utf-8')
    password=hashfun(encuser,encpas).decode('utf-8')

    return [username,password]


if __name__=="__main__":
    print(hashdata("A",'A')[1])