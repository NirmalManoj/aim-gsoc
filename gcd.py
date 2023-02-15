n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))

# greatest common divisor
while n1%n2!=0:
    r=n1%n2
    n1=n2
    n2=r
gcd=n2
print("GCD:",gcd)