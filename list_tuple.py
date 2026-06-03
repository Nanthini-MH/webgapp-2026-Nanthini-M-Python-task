students=input("Enter student name:").split()
marks=tuple(map(int,input("enter marks").split()))
dept=list(input("enter dept:").split())
def check_grade (mark):
    if mark>50:
        return "pass"
    else:
        return "fail"

for i in range(len(marks)):
    res=check_grade(marks[i])
    print("Student Name :",students[i])
    print("Department :",dept[i])
    print("Mark :",marks[i])
    print("Grade :",res)
    print("\n")

i=0
pass_count=0
fail_count=0
while i<(len(marks)):
    if(marks[i])>50:
        pass_count=pass_count+1
        i=i+1
    else:
        fail_count=fail_count+1
        i=i+1

print("Total No.of Students Pass:",pass_count)
print("Total No.of Students Fails:",fail_count)
