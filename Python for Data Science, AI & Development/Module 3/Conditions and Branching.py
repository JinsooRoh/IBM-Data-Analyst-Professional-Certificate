# Comparison operations
# 1. Equaility operator
age = 25
if age == 25:
    print("You are 25 years old.")

# 2. Inequality operator
if age != 30:
    print("You are not 30 years old.")

# 3. Greater than and less than
if age>= 20:
    print("Yes, the Age is greater than 20")

# Branching
# 1. The IF statement
age = 20
if age >= 21:
    print("You can enter the bar.")
else:
    print("Sorry, you cannot enter.")

# 2. The ELIF Statement
if age >= 21:
    print("You can enter the bar.")
elif age >= 18:
    print("You can watch a movie.")
else:
    print("Sorry, you cannot do either.")

# 3. Real-life example: Automated Teller Machine (ATM)
user_choice = "Withdraw Cash"
if user_choice == "Withdraw Cash":
    amount = input("Enter the amount to withdraw: ")
    if amount % 10 == 0:
        dispense_cash(amount) # type: ignore
    else:
        print("Please enter a multiple of 10.")
else:
    print("Thank you for using the ATM.")

# Logical operators
# 1. The NOT oeprator
# Real-life example: Notification settings
is_do_not_disturb = True
if not is_do_not_disturb:
    send_notification("New message received") # type: ignore

# 2. The AND operator
# Real-life example: Access control
has_valid_id_card = True
has_matching_fingerprint = True
if has_valid_id_card and has_matching_fingerprint:
    open_high_security_door() # type: ignore

# 3. The OR operator
# Real-life example: Movie night decision
friend1_likes_comedy = True
friend2_likes_action = False
friend3_likes_drama = False
if friend1_likes_comedy or friend2_likes_action or friend3_likes_drama:
    choose_a_movie() # type: ignore

