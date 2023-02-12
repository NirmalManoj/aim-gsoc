
# greatest common divisor
# Function to find gcd of two numbers
def gcd(num1, num2):
	# Find minimum of a and b
	result = min(num1, num2)

	while result:
		if num1 % result == 0 and num2 % result == 0:
			break
		result -= 1

	# Return the gcd of a and b
	return result

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("The GCD of", num1, "and", num2, "is", gcd(num1,num2))
