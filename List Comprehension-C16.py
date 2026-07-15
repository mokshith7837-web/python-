# ------------------------------------
# LIST COMPREHENSION
# ------------------------------------

# Task 1
a = ["mokshith", "eshanth", "kalyan", "dhanush"]
#output:["MOKSHITH","ESHANTH","KALYAN","DHANUSH"]

for i in a:
    print(i.upper(), end=" ")#we can't list method in this
print()

b = []
for i in a:
    b.append(i.upper())
print(b)#we can correct output



#syatax
#a = [expr for var in collection/range]


a = ["mokshith","eshanth","kalyan","dhanush"]
a = [i.upper() for i in a]
print(a)

# Task 2
b = ["vja", "hyd", "vzg"]
b = [i.title() for i in b]
print(b)

# Task 3
a = [1, 2, 3, 5, 6, 8, 12, 13]

print([i * i for i in a])
print([i ** 2 for i in a])
print([pow(i, 2) for i in a])

# ------------------------------------
# List Comprehension with if
# ------------------------------------

# Task 4
# Even numbers
even_numbers = [i for i in range(16) if i % 2 == 0]
print(even_numbers)

# Task 5
# Odd numbers
odd_numbers = [i for i in range(16) if i % 2 != 0]
print(odd_numbers)

# Task 6
# 0 to 30
print_nums = [i for i in range(31)]
print(print_nums)

# Task 7
# Fruits containing 'a'
fruits = ["apple", "banana", "grapes", "kiwi", "mango", "dragon", "berry"]
fruit = [i for i in fruits if "a" in i]
print(fruit)

# Task 8
# Fruits not containing 'a'
fruit = [i for i in fruits if "a" not in i]
print(fruit)

# ------------------------------------
# if-else in List Comprehension
# ------------------------------------

#Task-9
#range(21)-> even numbers-> Do Squares 
#range(21)-> odd numbers -> Do Multiply by 5

result = [i**2 if i % 2 == 0 else i * 5 for i in range(21)]
print(result)

# Task-10
a = [1, 2, 3, 4, 5]
b = [5, 4, 3, 2, 1]
#output = [6,6,6,6,6]

c = [a[i] + b[i] for i in range(len(a))]
print(c)

#without len()
c = [a[i]+b[i] for i in range(5)]
print(c)

