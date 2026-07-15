# -------------------------------
# Normal Method
# -------------------------------

a = 10
b = 20
print("The sum is:", a + b)
print("The difference is:", a - b)
print("The product is:", a * b)
print("The integer division is:", a // b)
print("The modulus is:", a % b)
print("The power is:", a ** b)

a = 30
b = 40
print("The sum is:", a + b)
print("The difference is:", a - b)
print("The product is:", a * b)
print("The integer division is:", a // b)
print("The modulus is:", a % b)
print("The power is:", a ** b)

a = 54
b = 2
print("The sum is:", a + b)
print("The difference is:", a - b)
print("The product is:", a * b)
print("The integer division is:", a // b)
print("The modulus is:", a % b)
print("The power is:", a ** b)

# -------------------------------
# Function
# -------------------------------

def calculate(a, b):
    print("The sum is:", a + b)
    print("The difference is:", a - b)
    print("The product is:", a * b)
    print("The integer division is:", a // b)
    print("The modulus is:", a % b)
    print("The power is:", a ** b)

calculate(10, 20)
calculate(30, 40)
calculate(54, 2)

# -------------------------------
# Function with User Input
# -------------------------------

while True:
    def add():
        a = int(input("Enter a value: "))
        b = int(input("Enter b value: "))
        print("Sum =", a + b)

    add()

    choice = input("Do you want to continue? (yes/no): ")
    if choice.lower() != "yes":
        break

# -------------------------------
# Full Name Function
# -------------------------------

def fullname():
    fname = input("Enter first name: ")
    lname = input("Enter last name: ")
    print((fname + " " + lname).title())

fullname()

# -------------------------------
# Function using print
# -------------------------------

def mul(a, b):
    print(a * b)

mul(4, 6)

# -------------------------------
# Function using return
# -------------------------------

def mul(a, b):
    return a * b

print(mul(7, 3))

# -------------------------------
# Print vs Return
# -------------------------------

def cal(a, b):
    c = a + b
    d = a - b
    e = a * b
    print(c)
    print(d)
    print(e)

cal(4, 3)

def cal(a, b):
    c = a + b
    d = a - b
    e = a * b
    return c, d, e

print(cal(2, 3))

# -------------------------------
# Split Bill
# -------------------------------

def splitbill():
    members = int(input("Enter total members: "))
    amount = int(input("Enter total amount: "))
    per_head = amount // members

    print("Per head bill is {}".format(per_head))
    print(f"Per head bill is {per_head}")

splitbill()
