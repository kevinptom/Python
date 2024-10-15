''' Python program to find first n odd numbers
Author:Kevin P Tom
Date:15-10-2024
Version: 1.0
'''
num=int(input("Enter a number:"))
sum=0
while(num>0):
    r=num%10
    sum=sum+r
    num=num//10
print(sum)