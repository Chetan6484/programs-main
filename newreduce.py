from functools import reduce
num=[1,2,3,4,5,6,7,8,9,10]
value=filter(lambda x:x%2==0,num)
value1=map(lambda x:x*x,value)
value2=reduce(lambda x,y:x+y,list(value1))
print(value2)