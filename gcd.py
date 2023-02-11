num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# greatest common divisor
result = 0
for i in range(1,num1):
    if num2%i == 0:
        if num1%i == 0:
            result = i

print("The GCD of", num1, "and", num2, "is", result)
