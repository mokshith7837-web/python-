# ------------------------------
# CONDITIONS IN PYTHON
# ------------------------------

# Comparison Operators
# <, >, <=, >=, !=, ==

a = 25
b = 54
if a < b:
    print("a is less than b")

a = 54
b = 25
if a > b:
    print("a is greater than b")

a = 17
b = 25
if a <= b:
    print("a is less than or equal to b")

a = 20
b = 40
if b >= a:
    print("b is greater than or equal to a")

a = 25
b = 17
if a != b:
    print("a and b are not equal")

a = 45
b = 45
if a == b:
    print("a and b are equal")

# User Input

a = int(input("Enter a value: "))
b = int(input("Enter b value: "))
if a < b:
    print("a is less than b")

a = int(input("Enter a value: "))
if a < 10:
    print("Less than 10")

a = "python"
if a == "java":
    print("True")

a = input("Enter a language: ")
if a == "java":
    print("True")

# ------------------------------
# Logical Operators
# and, or, not
# ------------------------------

a = 45
b = 25
if a <= b and b >= a:
    print("Condition is True")

a = 54
b = 25
if a <= b and b >= a:
    print("Condition is True")

a = 17
b = 25
if a != b and a == b:
    print("Condition is True")

a = 45
b = 25
if a <= b or b >= a:
    print("Condition is True")

a = 54
b = 25
if a <= b or b >= a:
    print("Condition is True")

a = 17
b = 25
if a != b or a == b:
    print("Condition is True")

a = 13
b = 15
if not a < b and b > a:
    print("Condition is True")

a = 17
b = 25
if not a < b or b > a:
    print("Condition is True")

a = int(input("Enter a: "))
b = int(input("Enter b: "))
if a < b and b > a:
    print("a is less than b")

# ------------------------------
# Identity Operators
# is, is not
# ------------------------------

# Integer
a = 5
if type(a) is int:
    print("It is an integer")

a = 25
if type(a) is not int:
    print("It is not an integer")

a = int(input("Enter an integer: "))
if type(a) is int:
    print("It is an integer")

# Float
a = 25.5
if type(a) is float:
    print("It is a float")

a = 25.5
if type(a) is not float:
    print("It is not a float")

a = float(input("Enter a float: "))
if type(a) is float:
    print("It is a float")

# String
a = "Mokshith"
if type(a) is str:
    print("It is a string")

a = input("Enter a string: ")
if type(a) is str:
    print("It is a string")

# ------------------------------
# Membership Operators
# in, not in
# ------------------------------

a = (2, 3, 4, 5, 6, 7, 8, 9, 10)

if 10 in a:
    print("10 is present")

if 20 in a:
    print("20 is present")

if 20 not in a:
    print("20 is not present")

# User input with membership operator

a = (2, 3, 4, 5, 6, 7, 8, 9, 10)
b = int(input("Enter a value: "))

if b in a:
    print("Value found")
else:
    print("Value not found")
