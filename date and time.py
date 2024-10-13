'''Python program to display date and time in different format
Author:Kevin P Tom
Date:08-10-2024
Version: 1.0'''
from datetime import datetime
current_time=datetime.now()
print(current_time)
format1=current_time.strftime("A,%B %d,%Y %H:%M:%S")
print(format1)
format2=current_time.strftime("%m/%d/%Y")
print(format2)
format3=current_time.strftime("%A,%B %d,%Y")
print(format3)
format4=current_time.strftime("%A,%B %d,%Y %H:%M:%S %p")
print(format4)
format5=current_time.strftime("%a-%b-%d %H:%M:%S IST %Y")
print(format5)
iso_format=current_time.isoformat()
print(iso_format)
format6=current_time.strftime('%d')
print(format6)
format7=current_time.strftime('%H:%M:%S')
print(format7)
format8=current_time.strftime('%m')
print(format8)
format9=current_time.strftime('%Y')
print(format9)