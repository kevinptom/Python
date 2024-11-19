list1 = []
list2 = []
list1_size = int(input("Enter the size of list1:"))
print('Enter the elements:')
for i in range(list1_size):
    list1.append(int(input()))
print(list1)
list2_size = int(input('Enter the size of list2:'))
print('Enter the elements: ')
for j in range(list2_size):
    list2.append(int(input()))
print(list2)
combined_list = list1 + list2
print(f'The combined list is:{combined_list}')

even_list=[]
odd_list = []
for i in combined_list:
    if(i%2==0):
       even_list.append(i)
    else:
       odd_list.append(i)

print(even_list)
print(odd_list)
even_list.sort()
odd_list.sort()
final_list = even_list + odd_list
print(f'The final list is:{final_list}')


