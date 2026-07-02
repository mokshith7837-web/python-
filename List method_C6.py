Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#list[]
a = [54,17.25,"python",9+7j,True,False]
print(a)
[54, 17.25, 'python', (9+7j), True, False]
type(a)
<class 'list'>
a = ["python","java","c"]
a.append("c++")
a
['python', 'java', 'c', 'c++']
a.append(["ml","ai"])
a
['python', 'java', 'c', 'c++', ['ml', 'ai']]


#extend()
a = ["kavya","mokshith","eshanth"]
a.extend(["kalyan","dhanush"])
a
['kavya', 'mokshith', 'eshanth', 'kalyan', 'dhanush']


#insert()
b = ["apple","banana","grapes"]
b.insert(1,"mango")
b
['apple', 'mango', 'banana', 'grapes']



#sort
a = ["mokshith","kavya","eshanth","kaylan","dhanush"]
a.sort()
a
['dhanush', 'eshanth', 'kavya', 'kaylan', 'mokshith']
b = [25,17,54,45,47]
b.sort()
b
[17, 25, 45, 47, 54]



#reverse()
a = ["c","java","html","css"]
a.reverse()
a
['css', 'html', 'java', 'c']
>>>  b = [17,25,54,45,47]
...  
SyntaxError: unexpected indent
>>> b = [17,25,54,45,47]
>>> b.reverse()
>>> b
[47, 45, 54, 25, 17]
>>> 
>>> 
>>> 
>>> #pop
>>> a = ["black","white","red","blue"]
>>> a.pop(2)
'red'
>>> a
['black', 'white', 'blue']
>>> 
>>> 
>>> #len()
>>> a = ['HI','hello','how']
>>> len(a)
3
>>>  b = ['hello']
...  
SyntaxError: unexpected indent
>>> b = ['hello']
>>> len(b)
1
>>> b = 'hello'
>>> len(b)
5
>>> 
>>> 
>>> 
>>> #count()
>>> a = ["mokshith","kavya","eshanth","kaylan","dhanush"]
>>> a.count('kavya')
1
