#dict 
# {"m":"sun","f":"house"}


# print(jaysonsComputer, type(jaysonsComputer))
# print(type(jaysonsComputer['year']))

#tuple = () parenthesis
#list = [] curly brackets
#sets = {'j', 'j','r', 'y'} curly_braces
#dict = {} curly_braces
# get()
# print(jaysonsComputer.get('model'))
# print(jaysonsComputer.keys())
# print(jaysonsComputer.values())

# print('Pro' == 'pro')

# if 'Pro' in jaysonsComputer['model']:
#     print("yes")
# else:
#     print(" no ")

jaysonsComputer = {
    "brand": {"HP", "macBook", 'Asus', 'Dell'},
    "model": ("Notebook",'Pro', 'Intel', 'AMD'),
    "year":["2021",'2020','2019','2018']
}
# print(jaysonsComputer['year'])

# for each in jaysonsComputer["year"]:    
#     print(each)

# r = 'rice'
# for d in r: 
#     print(d)
uk = ['machester', 'liverpool', 'westham', 'london']

# def jayson():
#     pass
#     return 

for q in uk:
    print(q)
    if q == 'liverpool':
        print("jayson hates liverpool")
        uk.append('leeds')
        continue

    classs = 'l'
    name = 'g'
    
print(name + ' | ' + classs)
# sandraisinourclass