class Person:
    def __init__(self,name):
        self.name=name
    def display(self):
        return f'Name :{self.name}'

class College:
    def __init__(self,college):
        self.college=college
    def display(self):
        return f'College Name:{self.college}'
    
class Dept(Person):
    def __init__(self,name,dept):
        super().__init__(name)
        self.dept=dept
    def display(self):
        print(super().display())
        return f'Dept:{self.dept}'

class Project(Dept):
    def __init__(self,name,dept,project_id):
        super().__init__(name,dept)
        self.project_id=project_id
    def display(self):
        print(Dept.display(self))
        return f'Project id: {self.project_id}'

class Student(Person,College):
    def __init__(self,student_id,name,college):
        super().__init__(name)
        College.__init__(self,college)
        self.student_id=student_id
    def display(self):
        print(Person.display(self))
        print(College.display(self))
        return f'Student id :{self.student_id}'

s2=Student("BCS17","Zayn","MSEC")
print(s2.display())
s=Project("Flynn","CSE","P01")
print(s.display())
