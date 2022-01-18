import datetime

# from datetime import datetime 
 
# print(datetime.now())  #>>>>>>>>>if line 3 is present in this scrip
# print(datetime.datetime.now())    #>>>>>>> if line 3 is not present in this script 
from datetime import datetime as g
# print(g.now())
# ''' you will only reference datetime.datetime if you didnt import datetime fom datetime '''

# #from now on i will assume import datetime.datetime is present 
print(g.now().date())
# print(datetime.now().time())
print(g.now().strftime("%H:%M:%S"))
print(g.now().strftime("%d:%m:%Y"))


#max()
#find()

#max()
# A a
# c = max(10,9,7,90)
# c = min(10,9,7,90)
# c = ('abc','bcd', 'ghj')
# list1 = ['PYNative', 'PYNAtive', 'PYnative']


# print(min(list1))

# def __str__(self, name, classs):
#     self.name = name
#     self.classs = classs

# def recaller(self):
#     print(self.name + "is here")

# r ="understand simple"
# v = 'un'
# c = r.find('as')
# print(r == v)
# print(c)




