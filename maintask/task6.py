# Write a program input a password. 
# Give them only 4 attempts to check the passwords entered against “admin@123”. 
# If the password is correct access is granted. After you show them a message , the account is blocked.

password = "admin@123"
attempts = 4

for i in range(0,4):
    code  = input("Enter your pin: ")
    if code == password:
        print("Access granted")
        break
    else:
        remaining = attempts - i
        if remaining > 0:
            print("Re-enter pin: ")
        else:
            print("Account is blocked")
