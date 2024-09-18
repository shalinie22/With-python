class calculater:

    def __init__(self,a,b):
        self.a = a
        self.b = b
    
    def addition(self):
        return self.a + self.b
    
    def subtraction(self):
        return abs(self.a - self.b)
    
    def multiplication(self):
        return self.a*self.b
    
    def division(self):
        return self.a//self.b
    
a= int(input("Enter the a number: "))

b = int(input("Enter the b number: "))
    
Calculater = calculater(a,b)

print("Add", Calculater.addition())
print("Sub", Calculater.subtraction())
print("Mul", Calculater.multiplication())
print("Div", Calculater.division())
