list = [1,3,1,12,78,98,3]
unique_list = []
for number in list:
    if number not in unique_list:
        unique_list.append(number)
print('The orginal list is:',list)
print(unique_list)

