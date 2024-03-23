# Continue with the program above, then use  the gross salary to find the NSSF. 
# To find the Kenya NSSF Rate using. Compute NSSF using 6% of the Gross Salary.
#  BUT ONLY A MAXIMUM OF 18,000 CAN BE USED IN NSSF. 

basic = float(input("Enter basic salary:  "))
benefits  = float(input("Enter bnefits: "))
gross = basic + benefits
nssf = gross * 0.06
if gross <= 18000:
    print(nssf)
else:
    print(18000*0.06)

# if gross < 6000:
#     nhif  = 150
# elif gross >= 6000 and gross < 8000:
#      nhif = 300
# elif gross >= 8000 and gross < 12000:
#     nhif = 400
# elif gross >= 12000 and gross < 15000:
#     nhif = 500
# elif gross >= 15000 and gross < 20000:
#     nhif = 600
# elif gross >= 20000 and gross < 25000:
#     nhif = 750
# elif gross >= 25000 and gross < 30000:
#     nhif = 850
# elif gross >= 30000 and gross < 35000:
#     nhif = 900
# elif gross >= 35000 and gross < 40000:
#     nhif = 950
# elif gross >= 40000 and gross <45000:
#     nhif = 1000
# elif gross >= 45000 and gross < 50000:
#     nhif = 1100
# elif gross >= 50000 and gross < 60000:
#     nhif = 1200
# elif gross >= 60000 and gross < 70000:
#     nhif = 1300
# elif gross >= 70000 and gross < 80000:
#     nhif =1400
# elif gross >= 80000 and gross < 90000:
#     nhif = 1500
# elif gross >= 90000 and gross < 100000:
#     nhif = 1600
# else:
#     nhif = 1700

# print("Your gross salary is Ksh. " f"{gross}")
# print("Your NHIF deduction is Ksh."f"{nhif}")