num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# greatest common divisor
if num1==0:
    result=num2

else:    
    while(num2 != 0):
        temp = num2
        num2 = num1 % num2
        num1 = temp
    result = num1   

print("The GCD of", num1, "and", num2, "is", result)
