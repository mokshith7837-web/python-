# -----------------------------------
# LOOPS IN PYTHON
# for, while, range, break, continue, pass
# -----------------------------------

# For loop with list
a = [17, 25, 45, 47, 54, 70, 80, 90]
for i in a:
    print(i)

# Print complete list each iteration
a = [17, 25, 45, 47, 54, 70, 80, 90]
for i in a:
    print(a)

# Print list elements in one line
a = [17, 25, 45, 47, 54, 70, 80, 90]
for i in a:
    print(i, end=",")
print()

# Print element type and list type
a = [17, 25, 45, 47, 54, 70, 80, 90]
for i in a:
    print(i)
    print(type(a))
    print(type(i))

# -----------------------------------
# Tuple
# -----------------------------------

a = [17, 25, 45, 47, 54, 70, 80, 90]
for i in a:
    print(i)

# -----------------------------------
# Set
# -----------------------------------

s = {54, 25, 17, 45, 47}
for i in s:
    print(i)

print(type(s))
print(type(i))


# -----------------------------------
# Dictionary
# -----------------------------------

d = {"year": 2006, "month": "July", "date": 29}

print("Keys")
for i in d:
    print(i)

print("Using keys()")
for i in d.keys():
    print(i)
    print(type(d))
    print(type(i))

print("Using values()")
for i in d.values():
    print(i)
    print(type(d))
    print(type(i))

print("Using items()")
for i in d.items():
    print(i)
    print(type(d))
    print(type(i))

# -----------------------------------
# String
# -----------------------------------

a = "codegnan"
for i in a:
    print(i)

# -----------------------------------
# Float List
# -----------------------------------

a = [1.7, 5.4]
for i in a:
    print(i)
print(type(a))
print(type(i))



# -----------------------------------
# String List
# -----------------------------------

a = ["Python", "Java", "HTML", "CSS"]
for i in a:
    print(i)

print(type(a))
print(type(i))

# -----------------------------------
# Complex Numbers
# -----------------------------------

a = [5 + 9j, 2 + 10j]
for i in a:
    print(i)

print(type(a))
print(type(i))

# -----------------------------------
# Boolean List
# -----------------------------------

a = [True, False]
for i in a:
    print(i)

print(type(a))
print(type(i))

# -----------------------------------
# Task 1
# -----------------------------------

fruits = ["apple", "banana", "mango"]

for i in fruits:
    print(i.upper(), end=",")
print()

fruit = str(fruits)
for i in fruit:
    print(i.upper(), end="")
print()

b = []
for i in fruits:
    b.append(i.upper())

print(b)

# -----------------------------------
# Task 2
# Output:
# [10,20,30,40,50,"code","c","o","d","e"]
# -----------------------------------

a = [10, 20, 30, 40, 50, "code"]

for i in a[-1]:
    a.append(i)

print(a)

a = [10, 20, 30, 40, 50, "code"]
a.extend("code")
print(a)

a = ["python", "java"]
a.extend(["c", "c++"])
print(a)

a.extend("html")
print(a)

# -----------------------------------
# Task 3
# Output: [2,3,4,5,6,7]
# -----------------------------------

a = [2, 3, 5, 6, 7]
a.insert(2, 4)
print(a)

# -----------------------------------
# Task 4
# Output: (5,6,7,8,9)
# -----------------------------------

b = (5, 6, 7, 8, 9, 10)

c = list(b)
c.remove(10)

d = tuple(c)
print(d)

# -----------------------------------
# Task 5
# Ascending Order
# -----------------------------------

e = [7, 9, 2, 0, 1, 4, 9, 17, 25, 54, 45, 47]
e.sort()
print(e)
