# Hierarchical Inheritance If multiple derived classes are created from the same base, this kind of Inheritance is known as hierarchical inheritance. In this instance, we have two base classes as a parent (base) class as well as two children (derived) classes.

# Python program for demonstrating Hierarchical inheritance  
  
# Here, we will create the Base class   
class Parent1:  
    def func_1(self):  
        print ("This function is defined inside the parent class.")  
  
# Derived class1  
class Child_1(Parent1):  
    def func_2(self):  
        print ("This function is defined inside the child 1.")  
  
# Derivied class2  
class Child_2(Parent1):  
    def func_3(self):  
        print ("This function is defined inside the child 2.")  
  
# Driver's code  
object1 = Child_1()  
object2 = Child_2()  
object1.func_1()  
object1.func_2()  
object2.func_1()  
object2.func_3() 