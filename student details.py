
'''Python program to get the student details
Author:Kevin P Tom
Date:01-10-2024
Version: 1.0'''

name=input('Enter the name of the student ')
roll_number=int(input("Enter the Rollnumber"))
roll_number=roll_number+1
CGPA=float(input('Enter your CGPA'))
Percentage=CGPA*10
print('Name of the student:',name)
print('Roll number of the student:',roll_number)
print('CGPA of the student=',CGPA)
print('Marks Percentage',Percentage,"%")