from datetime import datetime
current_time=datetime.now()
print(current_time)
format1=current_time.strftime("A,%B %d,%Y %H:%M:%S")
print("format1[YYYY-MM-DD HH:MM:SS]::--->",format1)
format2=current_time.strftime("%m/%d/%Y")
print("format2[MM/DD/YYYY]::--->",format2)
format3=current_time.strftime("%A,%B %d,%Y")
print(format3)
format4=current_time.strftime("%A,%B %d,%Y %H:%M:%S %p")
print(format4)
format5=current_time.strftime("%a-%b-%d %H:%M:%S IST %Y")
print(format5)
iso_format=current_time.isoformat()
print(iso_format)
format6=current_time.strftime('%m')
print(format6)