Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> # "-ve"-striding
>>> 
>>> a = "python course"
>>> a[-1:-11:-3]
'eu h'
>>> a[-2:-12:-4]
'sch'
>>> a[-5:-13:-5]
'oh'
>>> a[-13:-7:-1]
''
>>> a[-13:-7]
'python'
>>> a[-13:-7:1]
'python'
>>> a[-6::1]
'course'
>>> a[8:4:-2]
'o '
>>> a[::1]
'python course'
>>> a[::-1]
'esruoc nohtyp'
