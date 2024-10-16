''' Python program to determine the entry ticket
Author:Kevin P Tom
Date:15-10-2024
Version: 1.0
'''
age=int(input("Enter your age:"))
if age<10:
    print("Fare is 7")
elif age>=10 and age<60:
    print("Fare is 10")
else:
    print("Fare is 5")
