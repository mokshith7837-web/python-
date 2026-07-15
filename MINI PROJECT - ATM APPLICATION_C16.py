# -----------------------------------------
# MINI PROJECT: ATM APPLICATION
# -----------------------------------------

# Problem Statement:
#
# 1. The account balance is ₹100000.
#
# 2. Ask the user to insert the ATM card.
#    - If the user enters "c", print "Welcome 12345".
#    - Otherwise, print "Invalid Card".
#
# 3. If the card is valid, ask the user to enter the password.
#    - Password: "12345@2006"
#    - If the password is correct, display:
#         1. Balance Enquiry
#         2. Withdraw
#    - Otherwise, print "Incorrect Password".
#
# 4. If the user selects Balance Enquiry:
#    - Display the available account balance.
#
# 5. If the user selects Withdraw:
#    - Display the available balance.
#    - Ask the user to enter the withdrawal amount.
#    - If the withdrawal amount is less than or equal to the balance:
#         - Deduct the amount from the account.
#         - Display "Amount Withdrawn Successfully".
#         - Display the remaining account balance.
#    - Otherwise, print "Insufficient Balance".
#
# 6. If the user enters any option other than 1 or 2,
#    print "Invalid Option".
#
# Concepts Used:
# - input()
# - if, elif, else
# - Nested if
# - Variables
# - Arithmetic Operators
# - Comparison Operators


# ------------------------------------
# MINI PROJECT - ATM APPLICATION
# ------------------------------------

account_balance = 100000

insert_card = input("Insert ATM card (c): ")

if insert_card == "c":
    print("Welcome 12345")

    password = input("Enter Password: ")

    if password == "12345@2006":

        print("\n1. Balance Enquiry")
        print("2. Withdraw")

        option = int(input("Enter your option: "))

        if option == 1:
            print("Available Balance:", account_balance)

        elif option == 2:
            print("Available Balance:", account_balance)

            amount = int(input("Enter Withdraw Amount: "))

            if amount <= account_balance:
                account_balance -= amount
                print("Amount Withdrawn Successfully")
                print("Remaining Balance:", account_balance)
            else:
                print("Invalid! Insufficient Balance")

        else:
            print("Invalid Option")

    else:
        print("Incorrect Password")

else:
    print("Invalid Card")
