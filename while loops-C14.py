# -----------------------------------
# WHILE LOOP
# -----------------------------------

a = 17
while a > 1:
    print(a)
    a -= 1

print("----------------")

a = 29
while a > 1:
    print(a)
    a = a - 1

print("----------------")

a = 25
while a > 5:
    a = a - 1
    print(a)

print("----------------")

a = 25
while a > 5:
    a = a - 1
print(a)

print("----------------")

# Counting up
a = 2
while a <= 30:
    print(a)
    a += 1

print("----------------")

# Counting down
a = 30
while a > 2:
    print(a)
    a -= 1

print("----------------")

a = 5
while a < 25:
    print(a)
    a += 1

# -----------------------------------
# Voting
# -----------------------------------

while True:
    age = int(input("Enter your age (0 to exit): "))

    if age == 0:
        break

    if age >= 18:
        print("Eligible for voting")
    else:
        print("Not eligible for voting")

print("----------------")

# -----------------------------------
# Even or Odd
# -----------------------------------

num = int(input("Enter a number: "))

if num % 2 == 0:
    print("It is Even")
else:
    print("It is Odd")

print("----------------")

# -----------------------------------
# range()
# start, stop, step
# -----------------------------------

for i in range(10):
    print(i)

print("----------------")

for i in range(5, 15):
    print(i)

print("----------------")

for i in range(30, 45):
    print(i, end=",")
print()

print("----------------")

for i in range(2, 20, 2):
    print(i)

print("----------------")

for i in range(5, 50, 5):
    print(i)

print("----------------")

# -----------------------------------
# Grade Code
# -----------------------------------

while True:
    marks = int(input("Enter marks (-1 to exit): "))

    if marks == -1:
        break

    if marks in range(91, 101):
        print("Grade A")
    elif marks in range(81, 91):
        print("Grade B")
    elif marks in range(71, 81):
        print("Grade C")
    elif marks in range(50, 71):
        print("Grade D")
    elif marks in range(0, 50):
        print("Fail, Study Well")
    else:
        print("Invalid Marks")
