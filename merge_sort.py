import numpy as np

#creating an array
arr = np.array([4,9,6,5,7,8,3,1])

#sort using merge sort
sorted_arr = np.sort(arr, kind='mergesort')

print(f'the sorted array is: {sorted_arr}')

