def gcd(num1,num2,i):
    while i>0:
        if (num1%i)==0 and (num2%i)==0:
            return(i)
        else:
            i=i-1 

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
if num1<num2:
    i=num1
else:
    i=num2

# greatest common divisor
result = gcd(num1,num2,i)

print("The GCD of", num1, "and", num2, "is", result)
