num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
a=num1
b=num2
c=False
# greatest common divisor
if num1>=num2:
    c=num1%num2
    while num1%num2!=0:
        k=num1%num2
        num1=num2
        num2=k
        c=True
else:
    c=num2%num1
    while num2%num1!=0:
        k=num2%num1
        num2=num1
        num1=k
        c=True
if c==True:
    result=k
else:
    result=c

print("The GCD of", a, "and", b, "is", result)
