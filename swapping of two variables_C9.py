#swapping of two variables into four methods

#method-1
a = 25
b = 17
temp = a
a = b
b = temp
print(a)
print(b)
#(or)
print("after swapping a=%d,b=%d" %(a,b))

#method-2
a = 54
b = 45
a = a+b
b = a-b
a = a-b
print("a value is",a)
print("b value is",b)
#(or)
print("after swapping a=%d,b=%d" %(a,b))

#method-3
a = 47
b = 35
a = a^b
b = a^b
a = a^b
print("after swapping a value:", a)
print("after swapping b value:", b)

#method-4
a = 54
b = 25
a,b = b,a
print("after swapping a value:", a)
print("after swapping b value:", b)
 
