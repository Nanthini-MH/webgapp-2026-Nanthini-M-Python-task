class Student:
    def __init__(self,name):
        self.name=name

class Grade_calc(Student):
    def __init__(self,name,mark):
        super().__init__(name)
        self.mark=mark
    def calc_grade(self):
        if self.mark>50:
            print("Pass")
            self.status="pass"
        else:
            print("Fail")
            self.status="fail"

class Display(Grade_calc):
    def __init__(self,name,mark):
        Student.__init__(self,name)
        Grade_calc.__init__(self,name,mark)
    def display(self):
        print("Name:",self.name)
        print("Mark:",self.mark)
        Grade_calc.calc_grade(self)

# s=Display("Tom",87)
# s.display()
pass_count=0
fail_count=0
s1=[Display("tom",87),Display("alice",45),Display("john",98),Display("Martin",34),Display("Nancy",92)]
for i in range(len(s1)):
    print("----Student",i+1,"details----")
    s1[i].display()
    if s1[i].status=='pass':
       pass_count=pass_count+1
    else:
       fail_count=fail_count+1
print("Pass count:",pass_count)
print("Fail count:",fail_count)
