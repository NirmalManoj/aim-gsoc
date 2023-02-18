def gcd(num1,num2):
    if num2==0:
        return abs(num1)
    else:
        return gcd(num2,num1%num2)

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# greatest common divisor
result = gcd(num1,num2)

print("The GCD of", num1, "and", num2, "is", result)