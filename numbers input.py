'''Python program to perform arithmetic operations 
Author:Kevin P Tom
Date:08-10-2024
Version: 1.0'''
num1=int(input("Enter the first number"))
num2=int(input("Enter the second number"))
num3=int(input("Enter the third number"))
#add num1 and num2
sum=num1+num2
print("The sum of", num1, 'and', num2,' is:',sum)
#subtract num2 from num1
difference=num1-num2
print("The difference when ",num2, 'is subtracted from', num1 ,'is:',difference)
#multiply num1 by num2
product=num1*num2
print("the product of", num1," and", num2,"is:",product)
#divide num1 by num2
quotient=num1/num2
print("The quotient when" ,num1, "is divided by", num2 ,"is:",quotient)
#remainder of num1/num2
remainder=num1%num2
print("The reamainder when ",num1, "is divided by", num2 ,"is:",remainder)
#combined arithmetic operations
result=(num1+num2)*num3/2
print("The result of (",num1,'+',num2,')*',num3,"/2 is:",result)
