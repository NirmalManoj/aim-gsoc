# greatest common divisor

def gcd(num1,num2):
    while(num2):
       num1, num2 = num2, num1 % num2
    return abs(num1)

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))


result=gcd(num1,num2)

print("The GCD of", num1, "and", num2, "is", result)