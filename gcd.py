num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# greatest common divisor
for i in range(1,num1+1):
    if num1 % i == 0 and num2 % i == 0:
        gcd = i
result = gcd

print("The GCD of", num1, "and", num2, "is", result)
