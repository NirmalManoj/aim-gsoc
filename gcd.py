import math
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# greatest common divisor
result = math.gcd(num1 , num2)

print("The GCD of", num1, "and", num2, "is", result)
