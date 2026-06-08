marks=[85,96,36,88,45]
def check_grade(mark):
    if mark>50:
        return "pass"
    else:
        return "fail"
    
i=0
while i<len(marks):
    res=check_grade(marks[i])
    print("Student",i+1,res)
    i=i+1

for i in range(len(marks)):
    res=check_grade(marks[i])
    print("Student",i+1,res)