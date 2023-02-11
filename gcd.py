num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# greatest common divisor
def gcd(x,y):
    ans=0
    if x>=y:
        n=x
    else:
        n=y
    for i in range(1,n+1):
        if x%i==0 and y%i==0:
            ans=i
    return ans

print("The GCD of", num1, "and", num2, "is", gcd(num1,num2))
