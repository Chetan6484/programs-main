#program to find largest number without using max
def largest1(*number):
   largest=number[0];
   for num in number:
       if num>largest:
           largest=num;
   return largest
print(largest1(5,32,7,97,45))