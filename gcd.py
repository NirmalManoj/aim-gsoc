def get_gcd(num_1,num_2):
    if (num_1==num_2) or (num_2==0):
        return num_1
    if (num_1==0):
        return num_2
    else:
        if (num_1>num_2):
            return get_gcd(num_1-num_2,num_2)
        else:
            return get_gcd(num_1,num_2-num_1)
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# greatest common divisor
result = get_gcd(num1,num2)

print("The GCD of", num1, "and", num2, "is", result)
