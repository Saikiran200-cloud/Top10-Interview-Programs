import math 
pi = math.pi
def Circle(radius):
    return pi*(radius**2)
def Cube(side):
    return 6*side*side
def Cyclinder(radius,height):
    return 2*pi*radius + 2* pi *height
def Sphere(radius):
    return 2*pi*(radius **2)
print(Cyclinder(10,21))            