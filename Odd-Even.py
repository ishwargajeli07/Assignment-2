#Get an Integer from the user.
num = int(input("Enter a number: "))

#Determining whether the number is even or odd
a= num/2
if a==int(a):
    print(num,'is an even number.')
else:
    print(num, 'is an odd number.')