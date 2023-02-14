def gcd(a,b):
    result = min(a,b)
    while result:
        if a%result==0 and b%result ==0:
            break
        result-=1
        
    return result
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# greatest common divisor
gcd = gcd(num1,num2)

print("The GCD of", num1, "and", num2, "is", gcd)


