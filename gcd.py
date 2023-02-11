num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# greatest common divisor
def hcf(num1,num2):
    if(num2==0):
        return num1
    else:
        return hcf(num2,num1%num2)

print("The GCD of", num1, "and", num2, "is", hcf(num1,num2))
