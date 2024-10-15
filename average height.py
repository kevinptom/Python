'''' Python program to find average height of boys and girsls
Author:Kevin P Tom
Date:15-10-2024
Version: 1.0
'''
n=int(input("Enter number of students"))
btotal=0
tbh=0
gtotal=0
tgh=0
for i in range(1,n+1):
    Gender=input("Enter gender")
    Height=int(input("Enter height"))
    if Gender=="M":
        btotal+=1
        tbh=tbh+Height
    else:
        gtotal+=1
        tgh=tgh+Height
average_hb=tbh/btotal
print("Average height of boys",average_hb)
average_hg=tgh/gtotal
print("Average height of girls",average_hg)