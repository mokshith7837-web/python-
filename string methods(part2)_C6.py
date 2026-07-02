Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #title()
>>> name = "mokshith"
>>> sname = "karre"
>>> print(name+sname)
mokshithkarre
>>> print(name.title()+" "+sname.title())
Mokshith Karre
>>> print((name+" "+sname).title())
Mokshith Karre
>>> 
>>> 
>>> #formatting
>>> a = 25
>>> b = 17
>>> print("the sum is",a+b)
the sum is 42
>>> city = "palakollu"
>>> print("the city is",city)
the city is palakollu
>>> a = "sita"
>>> b = "ram"
>>> print(f"hello {a}{b}")
hello sitaram
>>> print(f"hello {a} {b}")
hello sita ram
>>> print(f"hello {a} hello {b}")
hello sita hello ram
>>> a = "kalyan"
>>> b = "dhanush"
>>> print("hello {}{}".format(a,b))
hello kalyandhanush
>>> print("hello {} {}".format(a,b))
hello kalyan dhanush
>>> print("hello {} hello {}".format(a,b))
hello kalyan hello dhanush
