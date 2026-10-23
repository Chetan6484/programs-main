#program to count even numbers in a list
def even (number):
    count=0
    for i in number:
        if i%2==0:
            count+=1
    return count
print(even([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]))