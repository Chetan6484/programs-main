#program to print names which have length greater than or equal to 4 using filter function
num=["sahil","rahul","ganesh","sam"]
r=list(filter(lambda num:len(num)>=4,num))
print(r)