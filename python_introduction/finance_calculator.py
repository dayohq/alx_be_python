# Prompt the user to input their financial details
monthly_income = int(input("Enter your monthly income:"))
monthly_expenses = int(input("Enter your total monthly expenses:"))
# Calculate Monthly Savings
monthly_savings = monthly_income - monthly_expenses
# Project Annual Savings
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)
#Output Results
print(monthly_savings)
print(projected_savings)
