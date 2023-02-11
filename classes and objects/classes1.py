# class basic code
class Hello:
    def __init__(self,name):
        self.name=name
    def first(self):
        print("Hello")

hai=Hello("shalinie")
same=hai.name
hai.first()
print(same)


# Example 2
class Hai:
    def func(self):
        print("hello world")

call=Hai()
call.func() 

#example 3

class course:
    def __init__(self):
        self.name="python"
        self.course="Data science"
    def first(self):
        name="python programming"
        print("func called", name)

courseobj=course()
courseobj.course="ML"
courseobj.first()
print(courseobj.course)



