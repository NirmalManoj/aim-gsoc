import math
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# greatest common divisor
print("The GCD of", num1, "and", num2, "is", end=" ")
print(math.gcd(num1,num2))