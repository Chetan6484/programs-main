def fibonacci_search(arr, target):
    n = len(arr)
    if n == 0:
        return -1
    fib_m2, fib_m1 = 0, 1
    fib_m = fib_m2 + fib_m1
    while fib_m < n:
        fib_m2 = fib_m1
        fib_m1 = fib_m
        fib_m = fib_m2 + fib_m1
    offset = -1
    
    while fib_m > 1:
        # Check if fib_m2 is a valid index
        i = min(offset + fib_m2, n - 1)
        if arr[i] < target:
            fib_m = fib_m1
            fib_m1 = fib_m2
            fib_m2 = fib_m - fib_m1
            offset = i
        elif arr[i] > target:
            fib_m = fib_m2
            fib_m1 = fib_m1 - fib_m2
            fib_m2 = fib_m - fib_m1
        else:
            return i
    if fib_m1 and offset + 1 < n and arr[offset + 1] == target:
        return offset + 1
    return -1
numbers = [10, 22, 35, 40, 45, 50, 55, 65, 70, 80]
print(fibonacci_search(numbers, 55)) 
print(fibonacci_search(numbers, 10))
print(fibonacci_search(numbers, 80))
print(fibonacci_search(numbers, 60)) 
