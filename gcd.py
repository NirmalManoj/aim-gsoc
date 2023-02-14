def gcd(a,b):
    if(b==0):
        return a
    return gcd(b,a%b)


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# greatest common divisor
result = gcd(num1,num2)

print("The GCD of", num1, "and", num2, "is", result)
