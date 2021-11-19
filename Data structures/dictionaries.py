'''
concatenation
operators
dictionaries
conditional statemets
loops

'''
# a = 'hello'
# b = 'world'

# print(a + ' ' +  b) #concatenate

quantity = 3
itemno = 567 
price = 49.95 
myorder = 'i want {1} pieces of item {0} for {2} dollars.'
print(myorder.format(quantity, itemno, price  ) )
print("dflfldf", itemno, 'dfjkfdkjfdkj')
demo = "we are writting \'python\' from the scratch "
print(demo) 
print("we are writing 'python' ")
print('we are writing \\(python)')

# operators
#arithmetic operators
#assignment operator
#comparison  ''
#logical
#identity
#membership
#bitwise

# + 
# -
# *
# / 
# %  
# ** exponentiation
print(2*2*2)
print(2**3)
#// 
x = 17
y = 2 
print(17/2)
print( x // y)
print(17 % 2)

# = 
# +=
q =4 
q +=6
print( q)
x =5 
# x += 3 
# print(x)
x-=2
print(x)
x*=20   #x *20
print(x)

x/=5 # x /5
print(x)

# comparison
#==
#!= 
#>
#<
#>=
#<=


#logical

#and 
#or
#not
x= 5

print( not(x> 3 and x < 10 ))


#python identity operators 
# is 
# is not 

# membership operators 
#in 
# not in

#bitwise operators
# & 
# | 
#^  
#~ 
#<<
#>>

# place = {'manchester', 'madrid', 'italy'}
# dicts = {
#     'places': 'chelsea',
#     'model': "lexus",
#     'food': ['amala', 'moi moi ', 'burger', 'pasta', 'eba and egusi soup']
    
# }
# print(len(dicts))
# print(dicts)

#  conditional statement
 
# if 4 > 7:
#     print("yes")
# else:
#     print("no")

# if 4 >= 7:
#     print("yes")
# else:
#     print("no")
    
# if 4 == 7:
#     print("yes")
# else:
#     print("no")

# if 4 != 7:
#     print("yes")
# else:
#     print("no")


if 4 == 7:
    print("yes")
elif(4>7):
    print("no")
else:
    print("equal")
