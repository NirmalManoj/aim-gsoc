num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
a=num1
b=num2
# greatest common divisor
while num1 != num2:
    if num1>num2:
        num1 -= num2
    else:
        num2 -= num1

print("The GCD of", a, "and", b, "is", result)
