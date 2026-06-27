Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
Datatype conversions
SyntaxError: invalid syntax
#int
int(9)
9
int(8.9)
8
int("mokshith")
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    int("mokshith")
ValueError: invalid literal for int() with base 10: 'mokshith'
int(6+9j)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    int(6+9j)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
int(Ture)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    int(Ture)
NameError: name 'Ture' is not defined


#float
float(8)
8.0
float(8.99)
8.99
float("mokshith")
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    float("mokshith")
ValueError: could not convert string to float: 'mokshith'
float(25+17j)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    float(25+17j)
TypeError: float() argument must be a string or a real number, not 'complex'
float(True)
1.0
float(False)
0.0


#string
str(54)
'54'
str("17.25")
'17.25'
str("kavya")
'kavya'
str(25+17j)
'(25+17j)'
str(True)
'True'
str(flase)
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    str(flase)
NameError: name 'flase' is not defined
str(Flase)
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    str(Flase)
NameError: name 'Flase' is not defined. Did you mean: 'False'?
str(False)
'False'




#boolean
>>> bool(4)
True
>>> bool(4.3)
True
>>> bool("kalyan")
True
>>> bool(True)
True
>>> bool(False)
False
>>> 
>>> 
>>> 
>>> 
>>> #complex
>>> complex(7)
(7+0j)
>>> complex(25.17)
(25.17+0j)
>>> complex("eshanth")
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    complex("eshanth")
ValueError: complex() arg is a malformed string
>>> complex("3+5j)
...         
SyntaxError: unterminated string literal (detected at line 1)
>>> complex(3+5j)
...         
(3+5j)
>>> complex(True)
...         
(1+0j)
>>> complex(kalyan)
...         
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    complex(kalyan)
NameError: name 'kalyan' is not defined
