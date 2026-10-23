def binary_search_recursive(arr, target, low, high):
    if low > high:
        return -1
    mid = (low + high) // 2
    if arr[mid] == target:
        return mid
    elif target < arr[mid]:
        return binary_search_recursive(arr, target, low, mid - 1)
    else:
        return binary_search_recursive(arr, target, mid + 1, high)
 
numbers = [5, 11, 18, 24, 31, 42, 56]
print(binary_search_recursive(numbers, 42, 0, len(numbers) - 1))
