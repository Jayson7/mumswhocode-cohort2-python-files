# basic maths quiz 

import datetime 


#>>>>>>>>>>>>>>>..greetings

def greeter():
    print("\n \n welcome to my brains basic maths quiz app")
    print("________________________________________________\n")
    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour <12:
        print(" Good Morning")
    elif hour >= 12 and hour < 18:
        print("Good Afternoon")
    elif hour >=18 and hour <24:
        print("Good Evening")
    else:
        print("Good Morning")
greeter()
