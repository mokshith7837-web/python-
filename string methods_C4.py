Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#string methods

# len()
a = "python"
len(a)
6
b = "kavya"
len(b)
5
c = "python course"
len(c)
13
d = ""
len(d)
0
e = " "
len(e)
1

# count()
a = ("kavya mokshith eshanth kalyan dhanush")
a.count("a")
6
a.count("kavya")
1
a.count("y")
2
a.count("v")
1
a.count("mokshith")
1


#find a string
a = "python"
a.find("t")
2
a.find("n")
5
b = "eshanth"
b.find("e")
0
b.find("n")
4


#escape sequences
#\n -> new line
#\t -> tab space
a = "name:mokshith\nmobilno:9849117847\tmailid:mokshith@gmail.com\clg:gvpce\ndept:IT"
print(a)
name:mokshith
mobilno:9849117847	mailid:mokshith@gmail.com\clg:gvpce
dept:IT
a = "name:mokshith\nmobilno:9849117847\tmailid:mokshith@gmail.com\nclg:gvpce\tdept:IT"
print(a)
name:mokshith
mobilno:9849117847	mailid:mokshith@gmail.com
clg:gvpce	dept:IT


#replace()

a = "wait until you succeed"
a.replace("wait","work")
'work until you succeed'
a.replace("you","get")
'wait until get succeed'
b = "i love java"
b.replace("java","python")
'i love python'
b
'i love java'
a
'wait until you succeed'



#upper(),capitalize(),islower(),title(),isdigit(),.isalpha(),startswith(),endswith()
a = "kavya"
a.upper()
'KAVYA'
a = "eshanth"
a.upper()
'ESHANTH'
a.capitalize()
'Eshanth'
e ="i am in class"
e.capitalize()
'I am in class'
e.title()
'I Am In Class'
a = "kavya"
a.isupper()
False
a.islower()
True
b = "ESHANTH"
b.isupper()
True
a.islower()
True
c = "12344"
c.isdigit()
True
b = "kalyan dhanush"
b.isalpha()
False
c = "kalyandhanush"
c.isalpha()
True
f = "mokahith_25"
f.isalnum()
False
f = "mokahith25"
f.isalnum()
True
g = "java"
KeyboardInterrupt
g.startswith("j")
True
g.endswith("a")
True
>>> 
>>> 
>>> 
>>> #strip()
>>> #lstrip() used to remove left side space
>>> #rstrip() used to remove right side space
>>> a = "         mokshith           "
>>> a.strip()
'mokshith'
>>> a.lstrip()
'mokshith           '
>>> b = "          kavya              "
>>> b.rstrip()
'          kavya'
>>> c =  "          mokshith kavya eshanth kalyan dhanush           "
>>> c.strip()
'mokshith kavya eshanth kalyan dhanush'
>>> 
>>> 
>>> #split()
>>> a = "mokshith kavya eshanth kalyan dhanush"
>>> a.split()
['mokshith', 'kavya', 'eshanth', 'kalyan', 'dhanush']
>>> d = "I am in class"
>>> d.split()
['I', 'am', 'in', 'class']
>>> 
>>> 
>>> #join()
>>> b = "kavya"
>>> "".join(b)
'kavya'
>>> a = 'mokshith', 'kavya', 'eshanth', 'kalyan', 'dhanush'
>>> "".join(a)
'mokshithkavyaeshanthkalyandhanush'
>>> "  ".join(a)
'mokshith  kavya  eshanth  kalyan  dhanush'
>>> "k".join(a)
'mokshithkkavyakeshanthkkalyankdhanush'
