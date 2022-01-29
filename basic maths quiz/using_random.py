# basic maths quiz 
import random
from random import randint
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
        
    # quit query 
    print("\n Press CTRL C to quit the app at any moment")

    # agreement 
    print("\n \t Rules")
    print("---------------------")
    print(""" 
          1. Each question goes for 20 points
          2. Wrong inputs of unrelated answers will result into failure 
          3. its just a simple maths quiz, dont freak out.
          
          """)
    
    print("\n Do you want to take the quiz")
    
    print("""
          
          1. Yes
          2. No 
          
          """)
greeter()


def exam():
    correct_ans = "Corect"
    wrong_ans = "Wrong"
    final_score = 0
    
    try:
        #question1
        a = randint(1,105)
        b = randint(105, 300)
        c = a * b
        print("first number", a)
        print('second number', b)
        question_one = input("What is the result of first number multiplied by second mumber: " )

        
        if int(question_one) == c:
            print(correct_ans)
            final_score += 20
        else:
            print(wrong_ans)
        
        
        #question2
        question_two = input("What is the result of 99 x 63?: ")
        answer_two = 6237
        
        if int(question_two) == answer_two:
            print(correct_ans)
            final_score += 20
        else:
            print(wrong_ans)
        
        #question3
        question_three = input("What is the result of 89 divided 23.4?: ")
        answer_three = 3.803
        answer_three_2 = 3.8034
        answer_three_3 = 3.80
        answer_three_4 = 3.8
        if float(question_three) == answer_three or float(question_three) == answer_three_2 or float(question_three) == answer_three_3 or float(question_three) == answer_three_4:
            print(correct_ans)
            final_score += 20
        else:
            print(wrong_ans)
        
        #question4
        question_four = input("What is the result of 102.45 x 56.2?: ")
        answer_four = 5757.69
        answer_four_2 = 5757
        answer_four_3 = 5758
        answer_four_4 = 5757.7
        
        if float(question_four) == answer_four or float(question_four) == answer_four_2 or float(question_four) == answer_four_3 or float(question_four) == answer_four_4:
            print(correct_ans)
            final_score += 20
        else:
            print(wrong_ans)
        
        #question5
        question_five = input("What is the result of 10237843 + 3892217?: ")
        answer_five = 14130060
        
        if int(question_five) == answer_five:
            print(correct_ans)
            final_score += 20
        else:
            print(wrong_ans)
            # grading
        if final_score >= 50:
            print("You Passed, your total score is", final_score) 
        else:
            print("You Failed, your total score is", final_score)
    except ValueError:
        print(wrong_ans)


    # check for errors on default gound
try:
    def consent_func():
        consent_reply = input("What's your take?: ")
        if int(consent_reply) == 1:
            exam()
        elif int(consent_reply) == 2:
            print("\n Alright, have a nice day")
        else:
            print("\n Come back when you are ready")
    consent_func()
except ValueError:
    print("\n Cant you listen to basic instructions")
    print("\n Game Over")
    
    
        

