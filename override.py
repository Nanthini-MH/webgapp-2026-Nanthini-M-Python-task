import math
class Shape:
    def area(self):
        return 0
    def perimeter(self):
        return 0
    
class Rectangle(Shape):
    def __init__(self,l,b):
        self.l=l
        self.b=b
    def area(self):
        return self.l*self.b
    def perimeter(self):
        return 2*(self.l+self.b)

class Triangle(Shape):
    def __init__(self,b,h):
        self.b=b
        self.h=h
    def area(self):
        return 0.5*self.b*self.h
    def perimeter(self):
        return self.b+self.h+(math.sqrt((self.b*self.b)+(self.h*self.h)))

s=[Rectangle(4,5),Triangle(6,7)]
for i in range(len(s)):
    print("area:",s[i].area())
    print("Perimeter:",s[i].perimeter())