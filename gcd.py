num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

def computeGCD(x, y):
 
    if x > y:
        small = y
    else:
        small = x
    for i in range(1, small + 1):
        if((x % i == 0) and (y % i == 0)):
            gcd = i
             
    return gcd
print("The GCD of", num1, "and", num2, "is", computeGCD(num1,num2))
