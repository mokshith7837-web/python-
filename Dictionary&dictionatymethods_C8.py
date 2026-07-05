Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #dictionary
>>> a = {"year":2026,"month":"july","date":6}
>>> a.update({"time":7})
>>> a
{'year': 2026, 'month': 'july', 'date': 6, 'time': 7}
>>> a.update({"name":"Mokshith","city":"palakollu"})
>>> a
{'year': 2026, 'month': 'july', 'date': 6, 'time': 7, 'name': 'Mokshith', 'city': 'palakollu'}
>>> 
>>> 
>>> #setdefault()
>>> a = {"course":"python"}
>>> a.setdefault("duration",4)
4
>>> a
{'course': 'python', 'duration': 4}
>>> 
>>> 
>>> 
>>> a = {'colour':'black','food':'biryani','icecream':'nuts'}
>>> a
{'colour': 'black', 'food': 'biryani', 'icecream': 'nuts'}
>>> #get()
>>> a.get('food')
'biryani'
>>> a
{'colour': 'black', 'food': 'biryani', 'icecream': 'nuts'}
>>> 
>>> 
>>> 
>>> #keys()
>>> a = {"month":7,"day":"sat","time":7}
>>> a.keys()
dict_keys(['month', 'day', 'time'])
>>> 
>>> 
>>> #values()
>>> a.values()
dict_values([7, 'sat', 7])
>>> 
>>> 
>>> 
>>> #items()
>>> a.items()
dict_items([('month', 7), ('day', 'sat'), ('time', 7)])



a = {"city":"palakollu","country":"india","state":"ap"}
#pop()
a.pop("city")
'palakollu'
a
{'country': 'india', 'state': 'ap'}
a.popitem()
('state', 'ap')
a
{'country': 'india'}



