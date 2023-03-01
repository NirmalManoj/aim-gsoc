num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# greatest common divisor
def gcd(a, b):
    if a == 0:
        return b
    if b == 0:
        return a

    if a == b:
        return a

    if a > b:
        return gcd(a-b, b)
    else:
        return gcd(a, b-a)

result = gcd(num1, num2)
print("The GCD of", num1, "and", num2, "is", result)
