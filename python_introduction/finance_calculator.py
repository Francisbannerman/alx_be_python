monthlyIncome = input("Enter your monthly income: ")
monthlyExpenses = input("Enter your total monthly expenses: ")
monthlyIncome = float(monthlyIncome)
monthlyExpenses = float(monthlyExpenses)
monthlySavings = monthlyIncome - monthlyExpenses
projectedSaving1 = monthlySavings * 12
projectedSaving2 = monthlySavings * 12 * 0.05
projectedSavings = projectedSaving1 + projectedSaving2
print("Your monthly savings are ",monthlySavings,)
print("Projected savings after one year, with interest, is: ",projectedSavings,)
