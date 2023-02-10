num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# greatest common divisor
small_number = min(num1, num2)
result = 1

for factor in range(small_number, 0, -1):
    if num1 % factor == 0 and num2 % factor == 0:
        result = factor
        break

print("The GCD of", num1, "and", num2, "is", result)
