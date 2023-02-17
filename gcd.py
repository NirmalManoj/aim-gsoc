num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# greatest common divisor
mini= min([num1,num2])
for i in range(1,min_num+1):
    if num1%i==0 and num2%i==0:
        result=i

print("The GCD of", num1, "and", num2, "is", result)
