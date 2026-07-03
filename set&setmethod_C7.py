Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#sets{}
a = {45,25.54,"kavya",47+46j,True,False}
print(a)
{False, True, 'kavya', 25.54, 45, (47+46j)}
type(a)
<class 'set'>


#issubset()
a = {2,3,4,5,6,4,6,65,3,3}
b = {5,6,3,6,3,5,4,3}
b.issubset(a)
True
a.issubset(b)
False
a = {1,2,3,5,67,43,4,4}
b = {6,3,6,3,5}
a.issuperset(b)
False


#union()
a ={1,2,33,4,5,6,7,4,2,1}
b= {1,2,4,5,6,7,8,9,9,4,3}
a.union(b)
{1, 2, 3, 4, 5, 6, 7, 8, 9, 33}


#intersection
a = {1,2,3,4,5,5,6,3,5,7,65,3,6,64,3}
b= {1,2,4,5,6,7,8,9,9,4,3}
a.intersection(b)
{1, 2, 3, 4, 5, 6, 7}


#difference
a = {1,2,3,4,5,5,6,3,5,7,65,3,6,64,3}
b= {1,2,4,5,6,7,8,9,9,4,3}
a.difference(b)
{64, 65}
b.difference(a)
{8, 9}


#syymmetric_differece
a = {1,2,4,5,6,7,8,9,9,4,3}
b= {1,2,4,5,6,7,8,9,9,4,3}
a.symmetric_difference(b)
set()
b = {6,3,6,3,5}
a.symmetric_difference(b)
{1, 2, 4, 7, 8, 9}


#update
a = {1,2,3,4,5,6,7,8}
b = {5,6,7,8,9}
a.update(b)
a
{1, 2, 3, 4, 5, 6, 7, 8, 9}


#intersection_updata()
a = {1,2,3,4,5,6,7,8,9,10}
b = {2,4,6,8,10,12,14,16}
a.intersection_update(b)
a
{2, 4, 6, 8, 10}
b.intersection_update(a)
b
{2, 4, 6, 8, 10}
a = {1,2,3,4,5,6,7,8,9,10}
b = {2,4,6,8,10,12,14,16}
a.intersection_update(b)
a
{2, 4, 6, 8, 10}



#difference_update
a = {2,4,6,8,10}
b = {2,4,6,8,10,12,14,16}
a.difference_update(b)
a
set()
b.difference_update(a)
b
{2, 4, 6, 8, 10, 12, 14, 16}


#symmetic_difference
a = {1,2,3,4,5,6,7,8,9}
b = {2,4,6,8,10,12,14,16}
a.symmetric_difference_update(b)
a
{1, 3, 5, 7, 9, 10, 12, 14, 16}
b.symmetric_difference_update(a)
b
{1, 2, 3, 4, 5, 6, 7, 8, 9}



#add(),copy(),clear()
a = {1,2,3,4,5,6,7,8,9}
a.add(10)
a
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
a.copy()
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
b = a.copy()
a.clear()
a
set()
c = set()
c.add(30)
c
{30}


#pop(),remove()
a = {5,6,7,8,9}
a.pop()
5
a.remove(7)
a
{6, 8, 9}
a.add(10)
a
{6, 8, 9, 10}

>>> 
>>> # discard
>>> a = {2,3,4,5,6}
>>> a.discard(4)
>>> a
{2, 3, 5, 6}
>>> 
>>> 
>>> #isdisjoint -> there should two oppsite sets
>>> a = {2,3,4,5,6,7}
>>> a.discard(4)
>>> a
{2, 3, 5, 6, 7}
>>> b = (4,5,6,7)
>>> b.isdisjoint(a)
Traceback (most recent call last):
  File "<pyshell#117>", line 1, in <module>
    b.isdisjoint(a)
AttributeError: 'tuple' object has no attribute 'isdisjoint'
>>> 
>>> 
>>> 
>>> #isdisjoint -> there should two oppsite sets
>>> a = {2,3,4,5,6,7}
>>> a.discard(4)
>>> a
{2, 3, 5, 6, 7}
>>> b = {4,5,6,7}
>>> b.isdisjoint(a)
False
>>> c = {8,9,10,11,12}
>>> b.isdisjoint(c)
True
>>> 
>>> 
>>> #len()
>>> a = {2,3,4,5,6,7}
>>> len(a)
6
