import numpy as np
# arr=np.array([1,2,3,4,5,7,8,9])
# print(arr)
# print(arr[2:7])
# print(arr[:6])
# print(arr[-5:])
matrix=np.array([[1,2,3],[2,3,4]])
row=np.array([1,2,3])
print(row+matrix)
arr=np.array([12,23,34,45,56])
print(np.sum(arr))

print(np.max(arr))

print(np.min(arr))

print(np.argmax(arr))

print(np.argmin(arr))

print(arr[arr>40])

print(arr[(arr<10) | (arr<30)])
print(arr[arr % 2 ==0])
print("\nRandom integers between 1 and 100:")
print(np.random.randint(1, 100, 5))
