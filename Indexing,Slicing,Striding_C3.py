Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#Indexing

a = "eshanth"
a[3]
'a'
# here the indexing is start from "zero"
#0,1,2,3,4,.....
a = "I am from palakollu"
a[5]+a[6]+a[7]+a[8]
'from'
a[10]+a[11]+a[12]+a[13]+a[14]+a[15]+a[16]+a[17]+a[18]
'palakollu'
a[0]
'I'
a = "simple is better than complex"
a[22]+a[23]+a[24]+a[25]+a[26]+a[27]+a[28]+a[21]+a[10]+a[11]+a[12]+a[13]+a[14]+a[15]+a[16]+a[0]+a[1]+a[2]+a[3]+a[4]+a[5]
'complex better simple'
a[22]+a[23]+a[24]+a[25]+a[26]+a[27]+a[28]
'complex'

a[0]+a[1]+a[2]+a[3]+a[4]+a[5]
'simple'
a[10]+a[11]+a[12]+a[13]+a[14]+a[15]+a[16]
'better '
b = "codegnan it solutions"
b[12]+b[13]+b[14]+b[15]+b[16]+b[17]+b[18]+b[19]
'solution'
b[0]+b[1]+b[2]+b[3]+b[4]+b[5]+b[6]+b[7]
'codegnan'


#"-ve" indexing
a = "I am learning Python"
a[-6]+a[-5]+a[-4]+a[-3]+a[-2]+a[-1]
'Python'
a[-15]+a[-14]+a[-13]+a[-12]+a[-11]+a[-10]+a[-9]+a[-8]
'learning'
a[-20]
'I'
a[-18]+a[-17]
'am'
b = "Python FullStack"
b[-5]+b[-4]+b[-3]+b[-2]+b[-1]
'Stack'
b[-9]+b[-8]+b[-7]+b[-6]
'Full'
b[-16]+b[-15]+b[-14]+b[-13]+b[-12]+b[-11]
'Python'
#here the "-ve" is start from last from -1,-2,-3,......


#slicing

a = "Time is very precious"
a[0:4:1]
'Time'
a[14:21:1]
'recious'
a[13:21:1]
'precious'
b = "work until you succeed"
b[15:22:1]
'succeed'
b[5:10:1]
'until'
b[0:4]
'work'
b[11:14]
'you'


#-ve slicing
a = "Vizag is city of destiny"
a[-15:-12]
'cit'
a[-7:]
'destiny'
a[-15:-11]
'city'
a[-24:-19]
'Vizag'
b = "Hi Kavya How are you"
b[-11:-8]
'How'
b[-17:-12]
'Kavya'
b[-7:-4]
'are'
b[-20:-18]
'Hi'


>>> 
>>> #Striding
>>> 
>>> a = "Data Science"
>>> a[::]
'Data Science'
>>> a[::1]
'Data Science'
>>> a[::2]
'Dt cec'
>>> a[::5]
'DSc'
>>> a[::2]
'Dt cec'
>>> a[3:11]
'a Scienc'
>>> a[9:]
'nce'
>>> a[::10]
'Dc'
>>> b ="Machine learning"
>>> b[::5]
'Mnag'
>>> b[::7]
'M n'
>>> b[::2]
'Mcielann'
>>> b[3:11]
'hine lea'
>>> b[:8]
'Machine '
>>> b[9:]
'earning'
>>> b[::4]
'Miln'
>>> b[::10]
'Ma'
>>> c = "Cloud computing"
>>> c[1:9:2]
'lu o'
>>> b[4:13:4]
'iln'
>>> c[::7]
'Cog'
>>> c[4:13:4]
'dmi'
