# Python program for demonstrating inheritance  
# Here, we will create the base class or the Parent class  
class Child1:  
  
    # here, we are apply the Constructor  
    def __init__(self, name):  
        self.name = name  
  
    # now, we will creat a class To get name  
    def getName1(self):  
        return self.name  
  
    # Now, we will create a class for checking   
    #if this person is student or not  
    def isStudent1(self):  
        return False  
  
# here, we will create the derived class or the child class  
class Student1(Child1):  
  
    # if the child is student, it will return true  
    def isStudent1(self):  
        return True  
  
  
# Driver code  
# An Object of Child  
std = Child1("Jackie")  
print(std.getName1(), std.isStudent1())  
  
# An Object of Student  
std = Student1("johnny")  
print(std.getName1(), std.isStudent1()) 