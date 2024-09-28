import numpy as np

arr =np.array([[[2,4,56],[4,6,7]],[[2,5,0],[[2,4,56]]]])


sum_of_row = []
for i in arr:
    sum = 0
    for x in i:
        sum += x
    sum_of_row.append(sum)
print(sum_of_row)

