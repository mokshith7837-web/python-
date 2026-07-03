Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #tuple()
>>> #tuple -> it is immutable
>>> a = (45,25.17,"mokshith",54+47j,True,False)
>>> print(a)
(45, 25.17, 'mokshith', (54+47j), True, False)
>>> type(a)
<class 'tuple'>
>>> #these are the methods present in the tuple
>>> len(a)
6
>>> a.index((54+47j))
3
>>> a.count(True)
1
