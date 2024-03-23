# Write a program called stars.
# It should prompt the user for a number, and it should print the number of stars till the number entered.
# Example If rows is 5, it should print the following:

stars = int(input("Enter number: "))
for i in range(0,stars+1):
    result = "*"* i
    print(result)
    
    
    
