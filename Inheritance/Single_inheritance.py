# Single Inheritance 
# Single inheritance allows a derivate class to inherit properties of one parent class, and this allows code reuse and the introduction of additional features in existing code.


class parentclass:
    
    def firstparent(self):
        print("Python programming")
    
    def secparent(self):
        print("R programming")

class child(parentclass):

    def firstchild(self):
        print("Django")

obj=child()
obj.firstchild()
obj.firstparent()
obj.secparent()

        