principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the interest rate (in percentage (1-100)): "))
time = float(input("Enter the number of years for the investment: "))

rate = rate/100

# Simple Interest Calculation
interest = (principal * rate * time)

print("The simple interest for an investment of", principal, "at", rate, "% for", time, "years is:", interest)
