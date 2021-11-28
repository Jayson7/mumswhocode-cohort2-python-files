import datetime

from datetime import datetime 
 
print(datetime.now())  #>>>>>>>>>if line 3 is present in this script
# print(datetime.datetime.now())    #>>>>>>> if line 3 is not present in this script 

''' you will only reference datetime.datetime if you didnt import datetime fom datetime '''

#from now on i will assume import datetime.datetime is present 
print(datetime.now().date())
print(datetime.now().time())
print(datetime.now().strftime("%H:%M:%S"))
