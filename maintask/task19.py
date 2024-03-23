# # Continue with the same program and find the person's PAYEE using the taxable income above.
#0 – 24,000	10%
# On the next 8,333	25%
# On the next 467,667	30%
# On the next 300,000	32.5%
# On amounts over 800,000	35%
# Personal Relief: KES 2,400.00 per month
# Minimum Taxable Income: KES 24,001.00 per month
basic = int(input("Enter basic salary: "))
benefits  = int(input("Enter benefits: "))
gross = basic + benefits
nssf = gross * 0.06
nhdf = gross * 0.015
relief = 2400
taxable = gross - (nssf + nhdf)


 
if taxable < 24001:
    paye = 0 
elif taxable > 24000 and taxable <= 32333:
    paye = (taxable - 24000)*0.25 + (0.1*24000) -(relief)
elif taxable > 32333 and taxable <= 500000:
    paye= (8233*0.25) + (0.1*24000)+ (taxable-32333)*0.3 - (relief)
elif taxable > 500000 and taxable <= 800000:
    paye= (8233*0.25) + (0.1*24000)+ (taxable-32333)*0.3 + (taxable-467667)*0.325 - (relief)
elif taxable > 800000:
    paye= (8233*0.25) + (0.1*24000)+ (taxable-32333)*0.3 + (taxable-467667)*0.325 + (taxable - 800000)*0.35 - (relief)

print(paye)

