'''' Python program to determine the entry ticket
Author:Kevin P Tom
Date:15-10-2024
Version: 1.0
'''
n=int(input("Enter a number:"))
f=1
while(n>0):
    f=f*n
    n-=1
print(f)