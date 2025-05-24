#!/usr/bin/python3
# A program to calculate simple interest based on principal, rate, and time

principal = 1000 #declare initial principal as $1000
rate = 0.05 #declare interest rate as 5%
time = 3 #declare time as 3 years

# Calculate simple interest using the formula: P * R * T
interest = float(principal * rate * time)

# Display the calculated interest to the user
print ("The simple interest is: ", interest)
