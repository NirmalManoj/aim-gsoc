def gcd(n1,n2) :
    gcd_list = []

    if n1<n2:
        smallest = n2
    else :
        smallest = n1

    for i in range(1,smallest+1):
        if (n1%i == 0 and n2%i == 0):
            gcd_list.append(i)
    
    return max(gcd_list)


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# greatest common divisor
result = gcd(num1,num2)

print("The GCD of", num1, "and", num2, "is", result)
