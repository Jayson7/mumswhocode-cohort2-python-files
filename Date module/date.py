'''
the datetime module isused to gather up things that has to do with date and time in python.

'''
# datetime 
import datetime 
from datetime import  time , date 

from datetime import datetime as  d  

#full datetime output
# print(d.now())

# print(dir(d.today))
# print(d.today())

# # year 
# name = 'myriam'
# print(f" the prof in the class is {name} ")
# print(datetime.datetime.now().year)
# print(datetime.datetime.now().strftime("%y"))
#%a
#%A
#%w
#%d
#%b
#%B
#%m
#y
# print(datetime.datetime.now().strftime("%B") )
#%p AM/PM


# #  only date 
# print(date.today())

# #  only time  using strif time
strTime = datetime.datetime.now().strftime("%H:%M:%S")   
print(strTime)


# strDate = datetime.datetime.now().strftime("%d:%m:%y")   
# print(strDate)
