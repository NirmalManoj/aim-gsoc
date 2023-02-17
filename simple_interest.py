principal = float(input())
rate = float(input())
time = float(input())

# Simple Interest Calculation
interest = (principal * rate * time / 100)

print("The simple interest for an investment of", principal, "at", rate, "% for", time, "years is:", interest)