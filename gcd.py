def HCF(num1, num2): '''This line will help you get the Highest common factor'''
    if num2==0:
        return num1
    else:
        return HCF(num2,num1%num2)
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# greatest common divisor
result = HCF(num1, num2)

print("The GCD of", num1, "and", num2, "is", result)

""" The above code will work in O(log(n)) Time complexity
    references:
    https://www.cuemath.com/numbers/greatest-common-divisor-gcd/
    https://www.cuemath.com/numbers/lcm-least-common-multiple/
    https://www.cuemath.com/numbers/hcf-highest-common-factor/
     ________________________________
    |Formulas:                       |
    |GCD=(a*b)/LCM(a,b)              |
    |LCM (a,b) = (a × b)/HCF(a,b)    |
    |________________________________|
    a=2
    b=5
    GCD=(a*b)/LCM(a,b)
    https://www.cuemath.com/numbers/greatest-common-divisor-gcd/

    Finding of LCM:
    https://www.cuemath.com/numbers/lcm-least-common-multiple/
    1.Write multiples of a examle: 2,4,6,8,10,....
      write multiples of b example: 5,10,...
      -->on writing a and b multiples check if match
        any a and b multiples if match break
    2.That match multiple is the LCM
    In that above exampl 10 was match
    LCM(2,5)=10
    LCM (a,b) = (a × b)/HCF(a,b)
    LCM (a,b) × HCF (a,b) = a × b
    
    Highest common factor
    https://www.cuemath.com/numbers/hcf-highest-common-factor/
    list the factors of a:1,2
    list the factors of b:1,5
"""
'''
This code will give the answer in the O(n) complexity it will even better also
HCF=None
common_factors=[]
if num1>num2:
    range_factor=num1
else:
    range_factor=num2
for each in range(1,range_factor+1):
    if (num1%each==0 and num2%each==0):
        common_factors.append(each)
HCF=common_factors[-1]
# print(HCF)
LCM=(num1*num2)//HCF
#print(LCM)
GCD=(num1*num2)//LCM
print("The GCD of", num1, "and", num2, "is", GCD)
'''