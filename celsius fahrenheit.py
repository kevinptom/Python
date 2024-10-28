temp=int(input("Enter temperature:"))
unit=input("Is this in Celsius or fahrenheit?")
if unit=="C":
	f=((9/5)*temp+32)
	print(temp,"Celsius is",f,"Fahrenheit")
else:
	c=5/9*(temp-32)
	print(temp,"Fahrenheit is",c,"Celsius")