import sqlite3 as sql

Con=sql.connect("users.db")
cursor=Con.cursor()

def Username_Password(username: str, password: int):
    try:
        query = "INSERT INTO users VALUES (?, ?)"
        cursor.execute(query,(username,password))
    except Exception  as  OperationalError :
                  
                  return 0
    except Exception as e:
            
            return 0
    return 1


Con.commit()

if(__name__=="__main__"):
       Username_Password("hello",121)
