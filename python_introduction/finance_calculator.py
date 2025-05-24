#!/usr/bin/python3
#A simple program to calculate the user's monthly savings based on inputted monthly income and expenses

monthly_income = int(input("Enter your monthly income: "))                  #prompt the user to enter their monthly income
monthly_expenses = int(input("Enter your total monthly expenses: "))        #prompt the user to enter their total monthly expenses
monthly_savings = monthly_income - monthly_expenses                         #calculate the users monthly savings
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)    #calculate their projected montlhy savings after an year

print (f"Your monthly savings are ${monthly_savings}.")                                #display the user's monthly savings
print (f"Projected savings after one year, with interest, is: ${projected_savings}.")  #display the user's projected savings