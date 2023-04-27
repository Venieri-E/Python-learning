pin = 1234
print("Please enter your pincode")
user_pin = int(input())

if pin == user_pin:
    print("Welcome, what amount you wish to withdraw?")
else:
    print("Incorect pincode , please try again , you have 2 tries")
    user_pin = int(input())
    if pin == user_pin:
        print("Welcome, what amount you wish to withdraw?")
    else:
        print("Incorect pincode , please try again , you have 1 try")
        user_pin = int(input())
        if pin == user_pin:
            print("Welcome, what amount you wish to withdraw?")
        else:
             print("Your card is blocked , please contact your bank")
