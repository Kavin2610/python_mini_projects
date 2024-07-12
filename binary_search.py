def bs(array, target):
    left = 0
    right = len(array)-1
    
    
    while (left <= right):
        middle = (left + right) // 2
        if array[middle] == target:
            return middle
        if target < array[middle]:
            right = middle - 1
        else:
            left = middle + 1
    return -1

print(f"The position of the target value is at {bs([1,2,3,4,5,6], 5)}")
