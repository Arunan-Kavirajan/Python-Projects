income = int(input("Enter your monthly income: "))
rent = int(input("Enter your monthly rent: "))
food = int(input("Enter your monthly food expenses: "))
transportation = int(input("Enter your monthly transportation expenses: "))
entertainment = int(input("Enter your monthly entertainment expenses: "))
savings = int(input("Enter your monthly savings expenses: "))
miscellaneous = int(input("Enter your monthly miscellaneous expenses: "))
expense = rent + food + transportation + entertainment + savings + miscellaneous
balance = income - expense

print(f"Monthly expense breakdown\nYour monthly income: {income}\nYour monthly expense: {expense}\nRemaining balance: {balance}")
print(f"Expense Breakdown:\nRent: ${rent} ({((rent/income)*100):.2f}%)\nFood: ${food} ({((food/income)*100):.2f}%)\nTransportaion: ${transportation} ({((transportation/income)*100):.2f}%)\nEntertainment: ${entertainment} ({((entertainment/income)*100):.2f}%)\nSavings: ${savings} ({((savings/income)*100):.2f}%)\nMiscellaneous: ${miscellaneous} ({((miscellaneous/income)*100):.2f}%)")
if expense < income:
    print(f"You've saved {balance} this month!")
else:
    print(f"Warning: Your expenses exceed your income by {expense-income}!\nYou might want to review your budget categories.")
