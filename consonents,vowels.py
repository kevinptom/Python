str=input("Enter a string")
vowels="aeiouAEIOU"
vowels_count=0
consonent_count=0
for char in str:
    if char in vowels:
        vowels_count+=1
    else:
        consonent_count+=1
print(f"The number of vowels in the given string {str}={vowels_count} ")
print(f"The number of consonent in the given string {str}={consonent_count} ")

