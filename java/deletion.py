def delete_element(arr, index):
    if 0 <= index < len(arr):
        deleted_value = arr[index]
        arr.pop(index)
        return deleted_value, arr
    raise IndexError("Invalid index")
 
numbers = [10, 20, 30, 40]
value, numbers = delete_element(numbers, 1)
print("Deleted:", value)
print("Array:", numbers)
