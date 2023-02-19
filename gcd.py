num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# greatest common divisor
def gcd(a,b):
    while (b != 0):
        rem = a % b
        a = b
        b = rem
    return a
    
result = gcd(num1, num2)

print("The GCD of", num1, "and", num2, "is", result)
