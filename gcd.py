num_1 = int(input("Enter first number: "))
num_2 = int(input("Enter second number: "))

def get_gcd(num_1, num_2):
	if(num_1 == num_2) or (num_2 == 0) :
		return num_1
	elif(num_1  == 0):
		return num_2
	else:
		if(num_1 > num_2) :
			return get_gcd(num_1 - num_2, num_2)
		else:
			return get_gcd(num_1, num_2 - num_1)

# greatest common divisor
result = get_gcd(num_1, num_2)

print("The GCD of", num_1, "and", num_2, "is", result)
