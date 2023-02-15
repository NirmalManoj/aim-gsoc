num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# greatest common divisor

def gcd(num1, num2):
    if num1 == 0:
        return num2

    return gcd(num2 % num1, num1)

result = gcd(num1,num2)

print("The GCD of", num1, "and", num2, "is", result)
