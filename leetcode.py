import numpy as np

# Swapping the first and last elements
arr = np.array([10, 20, 30, 40, 50])

arr[0], arr[-1] = arr[-1], arr[0]
print(arr)  