class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print("Name is ",self.name)
        print("Age of the ",self.name,"is",self.age)       
p1=Person("Tom",11)
p1.display()
p2=Person("Jerry",10)
p2.display()
 
