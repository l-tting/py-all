# Write a program that takes input of someone's basic salary and benefits, 
# adds them to find the gross salary then uses  the gross salary to find the NHIF. 
# To find the Kenya NHIF Rate using THIS LINK:  

basic = float(input("Enter basic salary:  "))
benefits  = float(input("Enter benefits: "))

def calc_gross(a,b):
    gross = a + b
    return gross
gross = basic + benefits
g_sal = calc_gross(basic,benefits)
print(f'Gross salary is {g_sal}')

def nhif(a):
    if a < 6000:
        nhif  = 150
    elif a >= 6000 and a < 8000:
        nhif = 300
    elif a >= 8000 and a < 12000:
        nhif = 400
    elif a >= 12000 and a < 15000:
        nhif = 500
    elif a >= 15000 and a < 20000:
        nhif = 600
    elif a >= 20000 and a < 25000:
        nhif = 750
    elif a >= 25000 and a < 30000:
        nhif = 850
    elif a >= 30000 and a < 35000:
        nhif = 900
    elif a >= 35000 and a < 40000:
        nhif = 950
    elif a >= 40000 and a <45000:
        nhif = 1000
    elif a >= 45000 and a < 50000:
        nhif = 1100
    elif a >= 50000 and a < 60000:
        nhif = 1200
    elif a >= 60000 and a < 70000:
        nhif = 1300
    elif a >= 70000 and a < 80000:
        nhif =1400
    elif a >= 80000 and a < 90000:
        nhif = 1500
    elif a >= 90000 and a < 100000:
        nhif = 1600
    else:
        nhif = 1700
    return nhif

nh = nhif(gross)
print(f"NHIF is KES.{nh}")


# Continue with the program above, then use  the gross salary to find the NSSF. 
# To find the Kenya NSSF Rate  using 6% of the Gross Salary. 
# BUT ONLY A MAXIMUM OF 18,000 Gross Salary CAN BE USED IN NSSF. 
def nssf(a,b=0.06):
    if a <= 18000:
        nssf = a * b
    else:
        nssf = 18000*b
    return nssf
gross = basic + benefits
ns = nssf(gross)
print(f'NSSF is KES.{ns}')


# Continue with the same program and calculate an individual’s NHDF using:
#  i.e NHDF = gross_salary *  0.015
def nhdf(a,b=0.015):
    nhdf = a * b
    return nhdf
nhd = nhdf(gross)
print(f'NHDF is KES.{nhd}')


#Calculate the taxable income.
#i.e taxable_income = gross salary - (NSSF + NHDF) 
def taxable_income(a,b,c):
    taxable= a - (b + c)
    return taxable
tax = taxable_income(gross,ns,nhd)
print(f"Taxable income is {tax}")

# Continue with the same program and find the person's PAYEE using the taxable income above.
# Find the Kenya PAYEE Tax Rate using THIS LINK
def payee(a,b):
    if a < 24001:
        paye = 0 
    elif a > 24000 and a <= 32333:
        paye = (a- 24000)*0.25 + (0.1*24000) -(b)
    elif a > 32333 and a <= 500000:
        paye= (8233*0.25) + (0.1*24000)+ (a-32333)*0.3 - (b)
    elif a > 500000 and a <= 800000:
        paye= (8233*0.25) + (0.1*24000)+ (a-32333)*0.3 +(a-467667)*0.325 - (b)
    elif a > 800000:
        paye= (8233*0.25) + (0.1*24000)+ (a-32333)*0.3 + (a-467667)*0.325 + (a - 800000)*0.35 - (b)

    return paye
relief = 2400
pay = payee(tax,relief)
print(f"PAYEE is {pay}")


#Continue with the same program and calculate an individual’s Net Salary using:
# net_salary = gross_salary - (nhif + nhdf +  nssf + payee)
def net_salary(a,b,c,d,e):
    net = a - (b + c + d + e)
    return net

net = net_salary(gross,nh,nhd,ns,pay)
print(f"Net salary is KES.{net}")



