num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# greatest common divisor
m=max(num1,num2)
n=min(num1,num2)
for i in range(1,n+1):
    if(m%i==0 and n%i==0):
        result=i


print("The GCD of", num1, "and", num2, "is", result)
