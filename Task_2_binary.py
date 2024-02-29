def binary_search(arr, x):
    low = 0
    high = len(arr)- 1
    mid = 0 
    count = 0

    while low <= high:
        mid  = (high + low) // 2
        count += 1

        if arr[mid] < x : 
            if x > arr[len(arr)-1]:
                return f'The upper limit is {x} itself'
            elif x <=  arr[mid + 1]:
                return (count, mid + 1)
            else:
                low = mid + 1
        
        elif x < arr[mid]:
            if arr[mid] == arr[0] and x < arr[mid]:
                return (count, mid)
            else:
                high = mid -1
        
        else:
            return (count, mid)
    

#arr = [1, 3, 4, 6, 8, 9, 12, 15]  #len = 8
#arr = [1/3, 2/5, 4/5, 4/7, 5/6, 8/9, 9/9] #len=7
arr = [2/7, 2/6 , 4/7, 4/5, 5/6, 8/9, 9/9]

#print(binary_search(arr, 7/8))
#print(binary_search(arr, 8/9))
result = binary_search(arr, 4/5)
print(f'The element(or the upper limit) at index {result[1]}, and it has been found at {result[0]} itarations')

