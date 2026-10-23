def get_element(arr, index):
    if 0 <= index < len(arr):
        return arr[index]
    raise IndexError("Invalid index")
 
def update_element(arr, index, new_value):
    if 0 <= index < len(arr):
        arr[index] = new_value
        return arr
    raise IndexError("Invalid index")
 
numbers = [5, 8, 12, 19]
print(get_element(numbers, 2))
numbers = update_element(numbers, 2, 15)
print(numbers)
