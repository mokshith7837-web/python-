# -----------------------------------
# IF-ELSE CONDITIONS IN PYTHON
# -----------------------------------

# Comparison Operators

a = 17
b = 25
if a < b:
    print("True")
else:
    print("False")

a = 45
b = 54
if a > b:
    print("True")
else:
    print("False")

a = 46
b = 47
if a != b:
    print("Not Equal")
else:
    print("Equal")

# -----------------------------------
# Logical Operators
# -----------------------------------

a = 17
b = 25

if a < b and b > a:
    print("Condition is True")
else:
    print("Condition is False")

if a < b or b > a:
    print("Condition is True")
else:
    print("Condition is False")

if not (a > b):
    print("Condition is True")
else:
    print("Condition is False")

# -----------------------------------
# Identity Operators
# -----------------------------------

a = 54
if type(a) is int:
    print("It is an integer")
else:
    print("It is not an integer")

a = 25
if type(a) is not int:
    print("It is not an integer")
else:
    print("It is an integer")

# -----------------------------------
# Membership Operators
# -----------------------------------

fruits = ["apple", "banana", "mango"]

if "banana" in fruits:
    print("Banana is present")
else:
    print("Banana is not present")

if "grapes" in fruits:
    print("Grapes is present")
else:
    print("Grapes is not present")

if "grapes" not in fruits:
    print("Grapes is not present")
else:
    print("Grapes is present")

if "apple" not in fruits:
    print("Apple is not present")
else:
    print("Apple is present")

# -----------------------------------
# IF-ELIF-ELSE
# -----------------------------------

a = 25
b = 54

if a < b:
    print("a is less than b")
elif b > a:
    print("b is greater than a")
else:
    print("Both are equal")

a = 45
b = 47

if a == b:
    print("Equal")
elif b > a:
    print("b is greater than a")
else:
    print("a is greater than b")

a = 17
b = 25

if a == b:
    print("Equal")
elif b < a:
    print("b is less than a")
elif a != b:
    print("Not Equal")
else:
    print("Equal")

# -----------------------------------
# MULTIPLE IF
# -----------------------------------

a = 17
b = 25

if a < b:
    print("a is less than b")

if b > a:
    print("b is greater than a")

if a != b:
    print("a and b are not equal")

a = 25
b = 40

if a < b:
    print("a is less than b")

if b > a:
    print("b is greater than a")

if a != b:
    print("a and b are not equal")

# -----------------------------------
# MULTIPLE IF USING LOGICAL OPERATORS
# -----------------------------------

a = 10
b = 20

if a < b and b > a:
    print("AND condition is True")

if a < b or b < a:
    print("OR condition is True")

if not (a > b):
    print("NOT condition is True")

# -----------------------------------
# MULTIPLE IF USING IDENTITY OPERATORS
# -----------------------------------

a = 25

if type(a) is int:
    print("Integer")

if type(a) is not float:
    print("Not Float")

if type(a) is not str:
    print("Not String")

# -----------------------------------
# MULTIPLE IF USING MEMBERSHIP OPERATORS
# -----------------------------------

numbers = (2, 3, 4, 5, 6, 7, 8, 9, 10)

if 5 in numbers:
    print("5 is present")

if 20 not in numbers:
    print("20 is not present")

if 10 in numbers:
    print("10 is present")

# -----------------------------------
# NESTED IF
# -----------------------------------

a = 4
b = 6

if a < b:
    print("Less")
    if b > a:
        print("Greater")

a = 25
b = 45

if a > b:
    print("Less")
    if b > a:
        print("Greater")

a = 2
b = 54

if a < b:
    print("Less")
    if b == a:
        print("Equal")

a = 17
b = 25

if a > b:
    print("Greater")
    if b > a:
        print("Less")
else:
    print("Condition is False")

a = 25
b = 45

if a < b:
    print("Less")
    if b > a:
        print("Greater")
    else:
        print("Equal")
else:
    print("False")

a = 17
b = 25

if a < b:
    print("Less")
    if b == a:
        print("Equal")
    elif a != b:
        print("Not Equal")

a = 25
b = 54

if a < b:
    print("Less")
    if b == a:
        print("Equal")
    elif a >= b:
        print("a is greater than or equal to b")
    else:
        print("a is less than b")
