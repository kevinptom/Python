check_number=int(input("Enter a number:"))
isPrime=True
for i in range(2,(check_number//2)+1):
    if check_number % i==0:
        isPrime=False
        break
if isPrime:
    print(f"The given number {check_number} is prime")
else:
    print(f"The given number {check_number} is not prime")

