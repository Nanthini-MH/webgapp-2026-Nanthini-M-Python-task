import numpy as np

# ==================================================
# 1. BROADCASTING
# ==================================================

print("========== BROADCASTING ==========")

arr = np.array([10, 20, 30, 40, 50])

print("Original Array:")
print(arr)

print("\nArray + 5:")
print(arr + 5)

print("\nArray * 2:")
print(arr * 2)

matrix = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

row = np.array([10, 20, 30])

print("\nMatrix:")
print(matrix)

print("\nRow Broadcasting:")
print(matrix + row)

column = np.array([
    [100],
    [200]
])

print("\nColumn Broadcasting:")
print(matrix + column)


# ==================================================
# 2. AGGREGATE FUNCTIONS
# ==================================================

print("\n========== AGGREGATE FUNCTIONS ==========")

marks = np.array([78, 45, 90, 32, 67, 88])

print("Marks:")
print(marks)

print("\nTotal Sum:")
print(np.sum(marks))

print("\nAverage:")
print(np.mean(marks))

print("\nMaximum Mark:")
print(np.max(marks))

print("\nMinimum Mark:")
print(np.min(marks))

print("\nCount:")
print(len(marks))

print("\nStandard Deviation:")
print(np.std(marks))

print("\nIndex of Maximum Mark:")
print(np.argmax(marks))

print("\nIndex of Minimum Mark:")
print(np.argmin(marks))


# ==================================================
# 3. FILTERING
# ==================================================

print("\n========== FILTERING ==========")

numbers = np.array([10, 25, 30, 45, 50, 65, 70, 85])

print("Numbers:")
print(numbers)

print("\nNumbers greater than 40:")
print(numbers[numbers > 40])

print("\nEven Numbers:")
print(numbers[numbers % 2 == 0])

print("\nOdd Numbers:")
print(numbers[numbers % 2 != 0])

print("\nNumbers between 30 and 70:")
print(numbers[(numbers >= 30) & (numbers <= 70)])

print("\nNumbers not equal to 50:")
print(numbers[numbers != 50])

marks = np.array([90, 20, 67, 34, 80])

print("\nMarks:")
print(marks)

print("\nPassed Marks:")
print(marks[marks >= 35])

print("\nFailed Marks:")
print(marks[marks < 35])


# ==================================================
# 4. RANDOM NUMBERS
# ==================================================

print("\n========== RANDOM NUMBERS ==========")

print("Random number between 0 and 1:")
print(np.random.rand())

print("\n5 random numbers between 0 and 1:")
print(np.random.rand(5))

print("\n2x3 random matrix between 0 and 1:")
print(np.random.rand(2, 3))

print("\nRandom 5 integers between 1 and 100:")
print(np.random.randint(1, 100, 5))

print("\nRandom 3x3 integer matrix:")
print(np.random.randint(1, 50, (3, 3)))

print("\nRandom choice from list:")
students = np.array(["Arun", "Kavin", "Santhosh", "Meena"])
print(np.random.choice(students))

print("\nShuffle array:")
data = np.array([1, 2, 3, 4, 5])
np.random.shuffle(data)
print(data)


# ==================================================
# 5. COMBINED MINI TASK
# ==================================================

print("\n========== MINI TASK ==========")

student_marks = np.random.randint(1, 101, 10)

print("Student Marks:")
print(student_marks)

print("\nAverage Mark:")
print(np.mean(student_marks))

print("\nHighest Mark:")
print(np.max(student_marks))

print("\nLowest Mark:")
print(np.min(student_marks))

print("\nPassed Students Marks:")
print(student_marks[student_marks >= 35])

print("\nFailed Students Marks:")
print(student_marks[student_marks < 35])

print("\nAdd 5 grace marks to all students:")
print(student_marks + 5)
