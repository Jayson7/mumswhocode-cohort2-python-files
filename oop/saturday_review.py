

class Human:
    def __init__(human_class, name, age):
        human_class.name = name
        human_class.age = age

    def myfunc(human_class):
        print("Hello my name is " + human_class.name)

h1 = Human("Tyler", 40)
h1.first_func()

# **********************

# del h1.age
print(h1.age)
# **********************
# pass 

# Python Inheritance***********************************

class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname()

# create the child class and do nothing
class Student(Person):
      pass
#  Use the pass keyword when you do not want to add any other properties or methods to the class.

# Add the __init__() Function**************************
# When you add the __init__() function, the child class will no longer inherit the parent's __init__() function.
#The child's __init__() function overrides the inheritance of the parent's __init__() function.

class Student(Person):
      def __init__(self, fname, lname):
          self.fname = fname
          self.name = fname
          
          
class Student(Person):
      def __init__(self, fname, lname):
        Person.__init__(self, fname, lname)

# use the super function
#Python also has a super() function that will make the child class inherit all the methods and properties from its parent:

class Student(Person):
      def __init__(self, fname, lname):
        super().__init__(fname, lname)

# By using the super() function, you do not have to use the name of the parent element, it will automatically inherit the methods and properties from its parent.

class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)
    self.graduationyear = 2019

x = Student("Mike", "Olsen")
print(x.graduationyear)
# -----------------------------------------
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

class Student(Person):
   def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year

x = Student("Mike", "Olsen", 2019)
print(x.graduationyear)
# If you add a method in the child class with the same name as a function in the parent class, the inheritance of the parent method will be overridden.
# -----------------------------------------------
