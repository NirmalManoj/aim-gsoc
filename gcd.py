num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if num1>num2:
    small = num2
else:
    small = num1
# greatest common divisor
for i in range(1, num2+1):
    if((num1%i == 0) and (num2%i == 0)):
        result = i

print("The GCD of", num1, "and", num2, "is",result)