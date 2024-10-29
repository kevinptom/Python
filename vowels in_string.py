str=input("Enter a string")
vowels="aeiouAEIOU"
vowels_count=0
for char in str:
    if char in vowels:
        vowels_count+=1
print(f"The number of vowels in the given string {str}={vowels_count} ")

