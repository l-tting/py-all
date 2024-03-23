from  datetime import datetime
# Write a program that takes the date of birth of a person 
# and the program outputs the age in terms of years,months,days TODAY.

today =  datetime.now()
dob = input("Enter  dob (dd/mm/yy)")
split_dob = dob.split("/")
# print(split_dob)
year_dob = int(split_dob[2])
month_dob = int(split_dob[1])
day_dob = int(split_dob[0])
dob_birth = datetime(day=day_dob,month=month_dob,year=year_dob)
age = today - dob_birth
years = age.days//365
month = (age.days%365)//31
days = (age.days%365)%31
print(years)
print(month)
print(days)
print(age)
# print(today)

