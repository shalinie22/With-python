class circle:

    def __init__(self,radius):
        self.radius = radius

    def area_of_circle(self):
        return 3.14 * (self.radius ** 2)
    
    def perimeter_of_circle(self):
        return 2 * 3.14 * self.radius
    
radius = int(input("Enter the radius: "))
getcirclevalues = circle(radius)

print(getcirclevalues.area_of_circle())
print(getcirclevalues.perimeter_of_circle())