'''Python program to display date and time in different format
Author:Kevin P Tom
Date:08-10-2024
Version: 1.0'''
n1=int(input("Enter the first number:"))
n2=int(input("Enter the second number:"))
n3=int(input("Enter the third number:"))
if n1>n2 and n1>n3:
        print("The largest number is:",n1)#print n1 is larger
elif n1<n2 and n2>n3 :
        print("The largest number is:",n2)#print n2 is larger 
else:
        print("The largest number is:",n3)#print n3 is larger