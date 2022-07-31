from datetime import datetime

today = datetime.today()
now = datetime.now()
utcnow = datetime.utcnow() 

str_now = (str)(now)
print(type(str_now))


print(f"{today} = datetime.today()")
print(f"{now} = datetime.now()")
print(f"{utcnow} = datetime.utcnow() ")
