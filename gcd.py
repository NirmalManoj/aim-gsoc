# function to calculate GCD
def gcd(num1, num2):
    if num2 == 0:
        return num1
    else:
        return gcd(num2, num1 % num2)

# get input from user
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# calculate GCD using the gcd() function
result = gcd(num1, num2)  #changed the operation

print("The GCD of", num1, "and", num2, "is", result)

