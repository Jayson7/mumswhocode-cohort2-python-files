'''
the datetime module isused to gather up things that has to do with date and time in python.

'''
# datetime 
import datetime 
from datetime import  time , date 
from datetime import datetime as  d  
# full datetime output
print(d.now())

# print(dir(d.today))
print(d.today())

# year 

print(datetime.datetime.now().year)
print(datetime.datetime.now().strftime("%A"))
print(datetime.datetime.now().strftime("%B") )



#  only date 
print(date.today())

#  only time  using strif time
strTime = datetime.datetime.now().strftime("%H:%M:%S")   
print(strTime)

strDate = datetime.datetime.now().strftime("%d:%m:%y")   
print(strDate)
