def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
 
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif target < arr[mid]:
            high = mid - 1         
        else:
            low = mid + 1           
    return -1
 
numbers = [5, 11, 18, 24, 31, 42, 56]
print(binary_search(numbers, 31))
print(binary_search(numbers, 20))
