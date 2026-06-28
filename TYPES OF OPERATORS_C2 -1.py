Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#Operation Type	Operators

#Arthematic Operators -> +,-,*,//,/,**,%
#Assignment Operators -> +=,-=,*=,//=,/=,**=,%=
#Comparision Operatos -> <,>,<=,>=,!=,==
#logical operators    -> and,or,not
#membership operators -> in,not in
#bitwise operators    -> &,|,~,^,<<,>>


#Arthematic Operators
a = 25
b = 17
print(a+b)
42
print(a-b)
8
print(a*b)
425
print(a/b)
1.4705882352941178
print(a//b)
1
print(a**b)
582076609134674072265625
print(a%b)
8


#Assignment Operators
a = 54
b = 45
a+b
99
a+=b
a
99
a-=b
a
54
a*=b
a
2430
a//=b
a
54
a/=b
a
1.2
a**=b
a
3657.261988008831
a%=b
a
12.26198800883094


#Comparision Operatos
a = 23
b = 45
a<b
True
b<a
False
b>a
True
a = 47
b = 47
a<=b
True
a>=b
True
a!=b
False
a==b
True
#logical operators    -> and,or,not

a = 17
b = 25
a<b and b>a
True
a<=b and b>=a
True
a!=b and a==b
False
a<b and b>a
True
a>b or b>a
True
a>=b or a<=b
True
a!=b or a==b
True
not True
False
not False
True



#membership operators
a = 25,17,54,45,47
17 in a
True
25 in a
True
True
True
55 not in a
True


#identify oprators
a=25
type(a) is int
True
type(a) is not int
False
a = 17.25
type(a) is float
True
True
True
type(a) is not float
False
a = "kayva"
type(a) is string
Traceback (most recent call last):
  File "<pyshell#84>", line 1, in <module>
    type(a) is string
NameError: name 'string' is not defined. Did you forget to import 'string'?
name = "kavya"
type(name) is str
True
a = 25+17j
type(name) is bool
False
type(a)
<class 'complex'>
type(a) is complex
True
a = True
type(a) is bool
True


#bitwise operators
a=45
b=47
a&b
45
a = 25
b = 17
a&b
17
b&a
17
bin(25)
'0b11001'
>>> bin(17)
'0b10001'
>>> bin(45)
'0b101101'
>>> bin(47)
'0b101111'
>>> bin(54)
'0b110110'
>>> #here bin is used to know the binary of numbers
>>> a|b
25
>>> a = 23
>>> b = 46
>>> a|b
63
>>> # here ~ -> -(a+1)
>>> a = 17
>>> ~a
-18
>>> b = 25
>>> ~b
-26
>>> c = -47
>>> ~c
46
>>> d = -45
>>> ~d
44
>>> e = +54
>>> ~e
-55
>>> a=25
>>> b=17
>>> a^b
8
>>> a = 54
>>> b = 47
>>> a^b
25
