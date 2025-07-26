#Get First number
a=int(input('Enter first no.: '))
#Get last number in the range
b=int(input('Enter last no.: '))

#Creating a list consisting all numbers in the given range.
list(range(a,b+1))
int_sum = 0

#Iterating loop over all the nos in the range
for i in range(a,b+1):
    int_sum += i

#Returns the ans
print('The sum of the numbers from' , a , "to", b, "is", int_sum)