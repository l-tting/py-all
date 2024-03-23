# Continue with the same program and calculate an individual’s Net Salary using:
#  net_salary = gross_salary - (nhif + nhdf +  nssf + payee)

basic = float(input("Enter basic salary: "))
benefits  = float(input("Enter benefits: "))
gross = basic + benefits
# nssf = gross * 0.06
nhdf = gross * 0.015
relief = 2400
# taxable = gross - (nssf + nhdf)



if gross <= 18000:
    nssf = gross * 0.06
else:
    nssf = (18000*0.06)
print(nssf)

taxable = gross - (nssf + nhdf)

if gross < 6000:
    nhif  =150
elif gross >= 6000 and gross < 8000:
     nhif = 300
elif gross >= 8000 and gross < 12000:
    nhif = 400
elif gross >= 12000 and gross < 15000:
    nhif = 500
elif gross >= 15000 and gross < 20000:
    nhif = 600
elif gross >= 20000 and gross < 25000:
    nhif = 750
elif gross >= 25000 and gross < 30000:
    nhif = 850
elif gross >= 30000 and gross < 35000:
    nhif = 900
elif gross >= 35000 and gross < 40000:
    nhif = 950
elif gross >= 40000 and gross <45000:
    nhif = 1000
elif gross >= 45000 and gross < 50000:
    nhif = 1100
elif gross >= 50000 and gross < 60000:
    nhif = 1200
elif gross >= 60000 and gross < 70000:
    nhif = 1300
elif gross >= 70000 and gross < 80000:
    nhif =1400
elif gross >= 80000 and gross < 90000:
    nhif = 1500
elif gross >= 90000 and gross < 100000:
    nhif = 1600
else:
    nhif = 1700
print(f"NHIF is {nhif}")

if taxable < 24000:
    paye = 0 
elif taxable >= 24000 and taxable <= 32333:
    paye = (taxable - 24000)*0.25 + (0.1*24000) - (relief)
elif taxable > 32333 and taxable <= 500000:
    paye= (8233*0.25) + (0.1*24000)+ (taxable-32333)*0.3 - (relief)
elif taxable > 500000 and taxable <= 800000:
    paye= (8233*0.25) + (0.1*24000)+ (467667*0.3) + (taxable-500000)*0.325 - (relief)
elif taxable > 800000:
    paye= (8233*0.25) + (0.1*24000)+ (467667*0.3) + (300000*0.325) + (taxable - 800000)*0.35 - (relief)

cut  = nhif +  nhdf + nssf + paye
net_salary = gross - cut
print(f"NHDF is {nhdf}")
print(f"Paye is {paye}")
print(f"Net salary is {net_salary}")

