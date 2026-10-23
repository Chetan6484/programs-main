from functools import reduce
def add(a,b):
    return a+b
num=[1,2,3,4,5,6]
result=reduce(add,num)
print(result)