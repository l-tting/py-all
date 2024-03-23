# Calculate the taxable income.
# i.e taxable_income = gross salary - (NSSF + NHDF) 

basic = int(input("Enter basic salary:  "))
benefits  = int(input("Enter benefits: "))
gross = basic + benefits
nssf = gross * 0.06
nhdf = gross * 0.015
taxable = gross - (nssf + nhdf)
print("Gross salary is Ksh."f"{gross}")
print("Taxable income is Ksh."f"{taxable}")