import numpy as np# the 'as' keyword hels to create an alias
#Array creation



#Data Science: is a branch of computer science where we study how to store, use and analyze data for deriving information from it.
#locality of reference - when something or data is stored continuously at one place in memory

#np.array is a function in numpy that creates an array object. The array object is a grid of values, all of the same type.
#The values in the array can be numbers, strings, or other types of data.
#The array object is a mutable object, meaning that it can be changed after it ris created.
#The array object is a sequence object, meaning that it can be indexed and sliced like a list
#The array object is a collection object, meaning that it can be iterated over like a list
#The array object is a mapping object, meaning that it can be used as a dictionary
#The array object is a set object, meaning that it can be used as a set
#The array object is a tuple object, meaning that it can be used as a tuple
#The array object is a list object, meaning that it can be used as a list
#The array object is a numpy object, meaning that it can be used as a numpy array
#The array object is a pandas object, meaning that it can be used as a pandas Series or
#DataFrame
#etc.

arr = np.array([1, 2, 3, 4, 5])

print(arr)
print(type(arr)) # prints out the type of array. in this case, it is an ndarray

#The ndarray is a homogeneous multidimensional array object in the Python NumPy library.
#It is the main data structure used in NumPy, and is the basis for all other data
#structures in NumPy.
#The ndarray is a subclass of the Python sequence type, and supports all the
#operations that are available for sequences, such as indexing, slicing, and
#iteration.

arr = np.array((1,2,3,4,5,6,7))

print(arr)


#Dimensions in Arrays
#A dimension is a way to describe the structure of an array. In NumPy, arrays can
 #have any number of dimensions, and the number of dimensions is called the rank of the array.
 #The rank of an array is also known as the number of axes.
 
arr = np.array(42) # 0-D Arrays

print(arr)

arr = np.array([1,2,3,4,5,6]) # 1-D Arrays don't be dumb

print(arr)

arr = np.array([[1,2,3],[4,5,6],[7,8,9]]) # 2-D Arrays

print(arr)

d = np.array([[[1,2,3],[1,2,3]] , [[1,2,3],[1,2,3]], [[1,2,3],[1,2,3]]])

print(d.ndim)



# indexing






arr =[[2,4,56],[4,6,7],[2,5,0]]

def sum_rows(arr):
    sum_of_row = []
    for i in arr:
        sum = 0
        for x in i:
            sum_of_row += x
        sum_of_row.append(sum_of_row)
    return sum_of_row

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
result = sum_rows(arr)
print(result)  # Output: [6, 15, 24]



def square_elements(arr):
    squared_arr = []
    for row in arr:
        squared_row = [element**2 for element in row]
        squared_arr.append(squared_row)
    return np.array(squared_arr)

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
result = square_elements(arr)
print(result)
# Output:
# [[ 1  4  9]
#  [16 25 36]
#  [49 64 81]]


