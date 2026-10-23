def count_down(n):
    if n==0:
        return 1 
    else:
        return n*count_down(n-1)
print(count_down(5))