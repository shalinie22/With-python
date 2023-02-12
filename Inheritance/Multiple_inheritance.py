# Multiple Inheritance If a class is able to be created from multiple base classes, this kind of Inheritance is known as multiple Inheritance. When there is multiple Inheritance, each of the attributes that are present in the classes of the base has been passed on to the class that is derived from it.

class parent1:
    fathername=""
    def father(self):
        print(self.fathername)

class parent2:
    mothername=""
    def mother(self):
        print(self.mothername)

class child1(parent1,parent2):
    def son(self):
        print("The mother name is",self.mothername)
        print("The father name is",self.fathername)

obj=child1()

obj.fathername="Perumal"
obj.mothername="Selvi"

obj.father()
obj.mother()
obj.son()
