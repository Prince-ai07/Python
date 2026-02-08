# Below is a system of the monthly contribution that someone will pay based on the gross income
gross_income = float(input("Enter gross income: "))
if gross_income > 0 and gross_income <= 5999:
    print(150.00)
elif gross_income > 5999 and gross_income <= 7999:
    print(300.00)
elif gross_income > 7999 and gross_income <= 11999:
    print(400.00)
elif gross_income > 11999 and gross_income <= 14999:
    print(500.00)
elif gross_income > 14999 and gross_income <= 19999:
    print(600.00)
elif gross_income > 19999 and gross_income <= 24999:
    print(750.00)
elif gross_income > 24999 and gross_income <= 29999:
    print(850.00)
elif gross_income > 29999 and gross_income <= 49999:
    print(1000.00)
elif gross_income > 49999 and gross_income <= 99999:
    print(1500.00)
else:
    print(2000.00)
