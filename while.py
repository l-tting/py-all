# # # # # # # # x = 34
# # # # # # # # while x < 50:
# # # # # # # #     print(x)
# # # # # # # #     x += 3

# # # # # # # # print("Task done for loop")

# # # pin = 5827
# # # pin_no = int()
# # # pin_tries = 0
# # # pin_limit = 4
# # # out_of_limit = False

# # # while pin_no != pin and not(out_of_limit):
# # #     if pin_tries < pin_limit:
# # #        pin_no = int(input("Enter your pin_no: "))
# # #        pin_tries +=1
# # #     else:
# # #         out_of_limit = True
# # # if out_of_limit == True:
# # #     print("Access blocked")
# # # else:
# # #     print("login successful")

# secret = '222'
# guess = ''
# while guess != secret :
#     guess = input("Enter guess: ")

# print("You got it!")
# # for num in range(19):
# #    print(num)a

pin = 5827
pin_no = int()
pin_tries = 0
pin_limits = 4
out_of_limit = False

while pin_no != pin and not(out_of_limit):
      if pin_tries < pin_limits:
        pin_no = int(input("Enter your pin_no: "))
        pin_tries += 1
      else:
        out_of_limit = True 
if out_of_limit==True:
     print("Access Denied")
else:
    print("Successful login")
