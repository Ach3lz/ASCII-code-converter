import numpy as np

ages = np.array([22,23,44,55,66,77])
# once you  are calling a method, you need to invoke it

x = np.where(77)
print(x)

# search sort works on sorted data

sorted_ages = np.sort(ages)
print(sorted_ages)


# if you want to sort you need to invoke the library.

sorted_ages = np.sort(ages)
print(sorted_ages)

# np.sort() returns a sorted copy of the array.
# np.sort() sorts the array in-place.

ages.sort()
print(ages)

# np.argsort() returns the indices that would sort the array.

indices = np.argsort(ages)
print(indices)

# np.searchsorted() finds the location where the value should be inserted to maintain sorted order in the array.

value = 50
index = np.searchsorted(ages, value)
print(index)

# np.concatenate() joins two arrays.

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr3 = np.concatenate((arr1, arr2))
print(arr3) 

# indexing

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr[0, 0])  # prints 1
print(arr[1, 1])  # prints 5
print(arr[2, 2])  # prints 9

# slicing

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr[:2, 1:])  # prints [[2, 3], [5, 6]]
print(arr[1:, :2])  # prints [[4], [5], [8]]

# broadcasting
