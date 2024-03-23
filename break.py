numbers = list(range(1,11))
attempt = 3
correct_pin = "1234"
for i in range(1,4):
    pin = input("Enter your pin: ")

    if pin == correct_pin:
        print("access granted")
        break
    else:
        remaining = attempt- i
        if remaining > 0:
            print("incorrect pin re-enter")
        else:
            print("blocked")