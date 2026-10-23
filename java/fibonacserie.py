def fibonacci_search(arr, target):
    n = len(arr)
    if n == 0:
        return -1
    
    # Initialize Fibonacci numbers
    fib_m2, fib_m1 = 0, 1
    fib_m = fib_m2 + fib_m1
    
    # Find the smallest Fibonacci number greater than or equal to n
    while fib_m < n:
        fib_m2 = fib_m1
        fib_m1 = fib_m
        fib_m = fib_m2 + fib_m1
        
    # Offset marks the eliminated front range of the array
    offset = -1
    
    while fib_m > 1:
        # Check if fib_m2 is a valid index
        i = min(offset + fib_m2, n - 1)
        
        # If target is greater than the value at index i, cut the subarray from offset to i
        if arr[i] < target:
            fib_m = fib_m1
            fib_m1 = fib_m2
            fib_m2 = fib_m - fib_m1
            offset = i
        # If target is less than the value at index i, cut the subarray after index i+1
        elif arr[i] > target:
            fib_m = fib_m2
            fib_m1 = fib_m1 - fib_m2
            fib_m2 = fib_m - fib_m1
        # Element found
        else:
            return i
            
    # Compare the last element if fib_m1 is 1
    if fib_m1 and offset + 1 < n and arr[offset + 1] == target:
        return offset + 1
        
    return -1

# Test Cases
numbers = [10, 22, 35, 40, 45, 50, 55, 65, 70, 80]
print(fibonacci_search(numbers, 55))  # Output: 6
print(fibonacci_search(numbers, 10))  # Output: 0
print(fibonacci_search(numbers, 80))  # Output: 9
print(fibonacci_search(numbers, 60))  # Output: -1
