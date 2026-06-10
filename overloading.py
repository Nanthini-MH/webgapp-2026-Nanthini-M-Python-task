class calculator:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
    def __add__(self, other):
        return calculator(self.x+other.x,self.y+other.y,self.z+other.z)
    def __sub__(self,other):
        return calculator(self.x-other.x,self.y-other.y,self.z-other.z)
    def __eq__(self,other):
        return calculator(self.x==other.x and self.y==other.y and self.z==other.z)
    def __repr__(self):#dunder method
        return f"calculator({self.x},{self.y},{self.z})"
    
c1=calculator(5,6,6)
c2=calculator(3,4,2)
c3=calculator(1,2,3)
# print(c1+c2)
# print(c1-c2)
# print(c1==c2)
c4=c1+c2+c3
print(c4)