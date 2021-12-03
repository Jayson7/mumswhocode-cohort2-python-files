# what is OOP*****************
'''
Object-oriented programming is a programming paradigm that provides a means of structuring programs so that properties and behaviors are bundled into individual objects.

For instance, an object could represent a person with properties like a name, age, and address and behaviors such as walking, talking, breathing, and running. Or it could represent an email with properties like a recipient list, subject, and body and behaviors like adding attachments and sending.

# ****
Put another way, object-oriented programming is an approach for modeling concrete, real-world things, like cars, as well as relations between things, like companies and employees, students and teachers, and so on. OOP models real-world entities as software objects that have some data associated with them and can perform certain functions.
'''



'''  
what is a class ?!**************
Classes are used to create user-defined data structures. Classes define functions called methods, which identify the behaviors and actions that an object created from the class can perform with its data.
A class, functions as a template that deﬁnes the basic characteristics of a particular object. Here's an example:
'''

# NB:Classes define functions called methods, which identify the behaviors and actions that an object created from the class can perform with its data.

# NB: an instance is an object that is built from a class and contains real data. An instance of the Dog class is not a blueprint anymore. It’s an actual dog with a name, like Miles, who’s four years old. Put another way, a class is like a form or questionnaire. An instance is like a form that has been filled out with information. Just like many people can fill out the same form with their own unique information, many instances can be created from a single class.

# How to Define a Class ************

class Sandra():
    pass



# __init__():  

# # Add the __init__() Function**************************
# # When you add the __init__() function, the child class will no longer inherit the parent's __init__() function.
# #The child's __init__() function overrides the inheritance of the parent's __init__() function.

# class Student(Person):
#       def __init__(self, fname, lname):
#           self.fname = fname
#           self.name = fname

class Human:
    def __init__(human_class, name, age):
        human_class.name = name
        human_class.age = age

    def myfunc(human_class):
        print("Hello my name is " + human_class.name)

h1 = Human("Tyler", 40)
h1.first_func()

# ***********************************


# class Dog:
#     species = "Canis familiaris"

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     # Instance method
#     def description(self):
#         return f"{self.name} is {self.age} years old"

#     # Another instance method
#     def speak(self, sound):
#         return f"{self.name} says {sound}"
    
# miles = Dog("Miles", 4)
# print(miles.description())


# # **********************

# # del h1.age
# print(h1.age)
# # **********************
# # pass 

# # Python Inheritance***********************************

# class Person:
#     def __init__(self, fname, lname):
#         self.firstname = fname
#         self.lastname = lname

#     def printname(self):
#         print(self.firstname, self.lastname)

# #Use the Person class to create an object, and then execute the printname method:

# x = Person("John", "Doe")
# x.printname()

# # create the child class and do nothing
# class Student(Person):
#       pass
# #  Use the pass keyword when you do not want to add any other properties or methods to the class.

          
          
# class Student(Person):
#       def __init__(self, fname, lname):
#         Person.__init__(self, fname, lname)

# # use the super function
# #Python also has a super() function that will make the child class inherit all the methods and properties from its parent:

# class Student(Person):
#       def __init__(self, fname, lname):
#         super().__init__(fname, lname)

# # By using the super() function, you do not have to use the name of the parent element, it will automatically inherit the methods and properties from its parent.

# class Person:
#     def __init__(self, fname, lname):
#         self.firstname = fname
#         self.lastname = lname

#     def printname(self):
#         print(self.firstname, self.lastname)

# class Student(Person):
#   def __init__(self, fname, lname):
#     super().__init__(fname, lname)
#     self.graduationyear = 2019

# x = Student("Mike", "Olsen")
# print(x.graduationyear)
# # -----------------------------------------
# class Person:
#     def __init__(self, fname, lname):
#         self.firstname = fname
#         self.lastname = lname

#     def printname(self):
#         print(self.firstname, self.lastname)

# class Student(Person):
#    def __init__(self, fname, lname, year):
#         super().__init__(fname, lname)
#         self.graduationyear = year

# x = Student("Mike", "Olsen", 2019)
# print(x.graduationyear)
# # If you add a method in the child class with the same name as a function in the parent class, the inheritance of the parent method will be overridden.
# # -----------------------------------------------
