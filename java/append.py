def append_element(arr, value):
    arr.append(value)
    return arr
 
def linear_search(arr, target):
    for index in range(len(arr)):
        if arr[index] == target:
            return index
    return -1
 
numbers = [1, 2, 3]
numbers = append_element(numbers, 4)
print(numbers)
print(linear_search(numbers, 3))
print(linear_search(numbers, 9))
