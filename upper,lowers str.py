def strings():
    sample_string=input("Enter the string")
    str1=sample_string.replace(" ","")
    no_of_uppercase = 0
    no_of_lowercase = 0
    for char in str1:
        if char.isupper():
            no_of_uppercase+=1

        else:
            no_of_lowercase+=1
    print(no_of_lowercase)
    print(no_of_uppercase)
strings()

