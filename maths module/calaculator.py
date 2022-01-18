# importing the module mathematics
import math

# framework
#library
# modules
# jquery
# react, vue , angular , django == djangorestframework
# socket, turtle , date, urlib, 
print(" Welcome to the world of python, choose a good option please")
print("This is a calculator")

print("choose one of the options available" '\n' '1: sin calculation ' '\n' '2: cos calculation,' '\n' '3: square root calculation'   '\n' '4: exp calculation' )
print("please be aware of the options available")

#checking the  state of the user's mindset 
options = input(" Enter your option please:  ")
# print(type(options))
c = int(options)


# options  
def sins():
    print("You have option 1 available")
    e = input("Please input your number: ")
    e_defined = int(e)
    sins_answer = math.sin(e_defined)
    print(sins_answer)

def cosins():
    print("You have option 3 available")
    e = input("Please input your number: ")
    e_defined = int(e)
    cosins_answer = math.cos(e_defined)
    print(cosins_answer)

def square_root():
    print("You have option 2 available")
    e = input("Please input your number: ")
    e_defined = int(e)
    sq_answer = math.sqrt(e_defined)
    print(sq_answer)
def exps():
    print("You have option 4 available")
    e = input("Please input your number: ")
    e_defined = int(e)
    exp_answer = math.exp(e_defined)
    print(exp_answer)
# ends

# options

if c == 1:
   sins()
elif c == 2:
    cosins() 
elif c == 3:
    square_root()
elif c == 4:
    exps()
else: 
    print(' why go against the rule ?!  ') 


# controller


