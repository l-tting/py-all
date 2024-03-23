# Continue with the same program and calculate an individual’s NHDF using:
#  i.e NHDF = gross_salary *  0.015

basic = int(input("Enter basic salary:  "))
benefits  = int(input("Enter benefits: "))
gross = basic + benefits
nhdf = gross * 0.015
print("Ksh."f"{nhdf}")