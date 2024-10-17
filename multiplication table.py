'''Python program to print multiplication table of input number
Author:Kevin P Tom
Date:08-10-2024
Version: 1.0'''
number=int(input("Enter a number"))
i=1
#using for loop to print multiplication table
for i in range(1,11,1):
    s=i*number
    print(number,"x",i,"=",s)
