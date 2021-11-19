
# A simple python counter using loop, conditional statements and exceptions

try:
    
    inputs = input("Enter your favourite number from range 1- 100: ")

    x = int(inputs)
    if x < 100:
        for i in range(101):
            print(i, 'counting')
            if i == 100:
                print('done')
            
    else:
        print("i refuse to count")
except ValueError:
    print(" i thought i asked for a number")
    
    
