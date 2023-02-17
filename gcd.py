num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# greatest common divisor
while num2:
    num1, num2 = num2, num1 % num2
result = num1

print("The GCD of", num1, "and", num2, "is", result)
