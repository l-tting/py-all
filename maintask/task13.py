# Write a program that takes the email and password as input from a user
# and checks if they are equal to “admin@mail.com” and password is “Admin@123” , 
# if so then print  “Login is Successful” and if not print “Invalid username or password”. 
# ONLY accept 3 tries after which it notifies you that you have been blocked.

# email = input("Enter your email: ")
# password = input("Enter password: ")
tries = 3
correct_email = "admin@mail.com"
correct_pass = "Admin@123"

for i in range(1,4):
    email = input("Enter your email: ")
    password = input("Enter password: ")
    if email == correct_email and password == correct_pass:
        print("Login successful")
        break
    else:
        attempt = tries - i
        if attempt > 0:
            print("Invalid username or password")  
        else:
            print("Access blocked")
