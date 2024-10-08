first_name=input('Enter your first name')
last_name=input('Enter your second name')
#concatenate two strings
full_name=first_name+' '+last_name
print(full_name)
#extract firstname
length=len(first_name)
print(length)
extracted_first_name=full_name[:length]
print(extracted_first_name)