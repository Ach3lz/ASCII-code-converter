#merge sort
# based on the concept of: divide conquer and combine.
# or split, sort and merge and repeat- at a fundamental standpoint
# the merge sort algorithm is a divide and conquer algorithm. It works by
# dividing a list into two halves, recursively sorting each half, and then
#=  merging the two sorted halves.
#arr ]
def merge_sort(arr):
    if len(arr)>1:
        mid = len(arr)//2
        left_half = arr[:mid]
        right_half = arr[mid:]
        # recursion - calling a the function in itself
        merge_sort(left_half)
        merge_sort(right_half)
        
        i=j=n=0
        while i < len(left_half) and j < len(right_half):
            if left_half[i]< right_half[j]:
                arr[n]=left_half[i]
                i += 1
            else:
                arr[n]= right_half[j]
                j += 1
            n += 1
            
            while i < len(left_half):
                arr[n]=left_half[i]
                i += 1
                n += 1
                
            while j < len(right_half):
                arr[n]= right_half[j]
                j +=1
                n +=1
                
arr =[4,9,6,5,7,8,3,1]
merge_sort(arr)
print(arr)

        
        
        

    


