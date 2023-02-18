num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# greatest common divisor
result=0
if(num1==0 and num2!=0):
    result=num2
elif(num2==0 and num1!=0)::
    result=num1
elif(num1==0 and num2==0):
    presult=0
else:
    for i in range(1,max(num1,num2)):
        if(num1 %i==0 and num2%i==0):
            result=i
print("The GCD of", num1, "and", num2, "is", result)
