# Multilevel inheritance, the features that are part of the original class, as well as the class that is derived from it, are passed on to the new class. It is similar to a relationship involving grandparents and children.

class grandfather:
    def __init__(self,grandfathername):

        self.grandfathername=grandfathername


class parent(grandfather):
    def __init__(self,grandfathername,parentname):
        self.parentname=parentname

         # here, we will invoke the constructor of Grandfather class 
        grandfather.__init__(self, grandfathername) 


class son(parent):
    def __init__(self, grandfathername, parentname,sonname):
        self.sonname=sonname

        parent.__init__(self,grandfathername,parentname)

    def output(self):
        print(self.grandfathername)
        print(self.parentname)
        print(self.sonname)

obj=son("Lee","jon","jin")

obj.sonname="jinn"
obj.grandfathername="Leee"
obj.parentname="john"

obj.output()