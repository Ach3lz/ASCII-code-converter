import numpy as np

arr = np.array([[1,2,3],[4,5,6],[7,8,9]])

squared_array = []

for i in arr:
    for x in i:
        squared_array.append(x**2)
        
print(squared_array)