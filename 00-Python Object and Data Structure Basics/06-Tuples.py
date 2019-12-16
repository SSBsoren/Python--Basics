Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
#####################################################333
>>> ########## Tuples
>>> ####################################################
>>> t = (3,2,4)
>>> t
(3, 2, 4)
>>> len(t)
3
>>> t[0]
3
>>> t[-1]
4
>>> t.idex
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    t.idex
AttributeError: 'tuple' object has no attribute 'idex'
>>> t.indes()
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    t.indes()
AttributeError: 'tuple' object has no attribute 'indes'
>>> t.index()
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    t.index()
TypeError: index() takes at least 1 argument (0 given)
>>> t.index('one')
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    t.index('one')
ValueError: tuple.index(x): x not in tuple
>>> t
(3, 2, 4)
>>> t.index('one')
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    t.index('one')
ValueError: tuple.index(x): x not in tuple
>>> t.count()
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    t.count()
TypeError: count() takes exactly one argument (0 given)
>>> t.count(0)
0
>>> t.index(1)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    t.index(1)
ValueError: tuple.index(x): x not in tuple
>>> t.append('3')
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    t.append('3')
AttributeError: 'tuple' object has no attribute 'append'
>>> t
(3, 2, 4)
>>> t = ('One',1,2,3)
>>> t.index(2)
2
>>> t.count(3)
1
>>> t[0] = 'Change'
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    t[0] = 'Change'
TypeError: 'tuple' object does not support item assignment
>>> 
#########################################################33333
>>> ##############    immutable meaning they can not be changed.
>>> ##############################################################
