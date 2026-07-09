# ---------------------------------------
# Task 1: Voting Eligibility
# ---------------------------------------

age = int(input("Enter the age of the voter: "))

if age >= 18:
    print("You can vote")
else:
    print("You can't vote")

# ---------------------------------------
# Task 2: Even or Odd
# ---------------------------------------

a = int(input("Enter a number: "))

if a % 2 == 0:
    print("Even")
else:
    print("Odd")

# ---------------------------------------
# Task 3: Leap Year
# ---------------------------------------

year = int(input("Enter a year: "))

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print("It is a Leap Year")
else:
    print("It is Not a Leap Year")

# ---------------------------------------
# Task 4: Guest Code
# ---------------------------------------

guest = input("Enter your name: ").lower()

if guest == "mokshith":
    print("Welcome", guest)
else:
    print("Welcome Guest")

# ---------------------------------------
# Task 5: Guest List
# ---------------------------------------

names = ["mokshith", "kavya", "kalyan", "eshanth", "dhanush"]

guest = input("Enter your name: ").lower()

if guest in names:
    print("Welcome", guest)
else:
    print("Welcome Guest")

# ---------------------------------------
# Task 6: Vowel or Consonant
# ---------------------------------------

letter = input("Enter a letter: ").lower()

if letter in "aeiou":
    print("It is a vowel")
else:
    print("It is a consonant")

# ---------------------------------------
# Task 7: Social Media Login (Nested if)
# ---------------------------------------

username = input("Enter your username: ")
password = input("Enter your password: ")

if username == "mokshith":
    print("Username is valid")
    if password == "12345@2006":
        print("Login Successful")
    else:
        print("Invalid Password")
else:
    print("Invalid Username")

# ---------------------------------------
# Task 8: Social Media Login (Logical Operator)
# ---------------------------------------

username = input("Enter your username: ")
password = input("Enter your password: ")

if username == "mokshith" and password == "12345@2006":
    print("Login Successful")
else:
    print("Invalid Username or Password")

# ---------------------------------------
# Task 9: Multiple if
# ---------------------------------------

age = int(input("Enter your age: "))
marks = int(input("Enter your marks: "))
attendance = int(input("Enter your attendance (%): "))

if age >= 18:
    print("Eligible for voting")

if marks >= 80:
    print("Eligible for internship")

if attendance >= 80:
    print("Eligible to attend the class")

# ---------------------------------------
# Task 10: Cake Menu (if-elif-else)
# ---------------------------------------

price = int(input("Enter the price of the cake: "))

if price == 1200:
    print("Red Velvet Cake")
elif price == 1000:
    print("Almond Cake")
elif price == 800:
    print("Chocolate Cake")
elif price == 600:
    print("Butterscotch Cake")
else:
    print("Cake is not available")

# ---------------------------------------
# Task 11: Pizza Menu (if-elif-else)
# ---------------------------------------

price = int(input("Enter the price: "))

if price == 1000:
    print("BBQ Pizza")
elif price == 800:
    print("Crispy Chicken Pizza")
elif price == 600:
    print("Paneer Pizza")
elif price == 400:
    print("Corn Pizza")
elif price == 200:
    print("French Fries & Coke")
else:
    print("Item not available")
