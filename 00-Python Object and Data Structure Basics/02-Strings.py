Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
=============================== RESTART: Shell ===============================
>>> 
=============================== RESTART: Shell ===============================
>>> ################### Strings
>>> #Single word
>>> 'sagen'
'sagen'
>>> 'Hello, this is Sagen'
'Hello, this is Sagen'
>>> print(" I'm Sagen"0
	  
SyntaxError: invalid syntax
>>> 
	  
>>> print(" I'm Sagen")
	  
 I'm Sagen
>>> print(' I'm Sagen')
	  
SyntaxError: invalid syntax
>>> print(" This is Sagen Soren\n Jamshedpur ")
	  
 This is Sagen Soren
 Jamshedpur 
>>> ####### String Index
	  
>>> a = 'Sagen Sakam Bhim Soren '
	  
>>> len(a)
	  
23
>>> a[3]
	  
'e'
>>> a[1]
	  
'a'
>>> a[S:}
	  
SyntaxError: invalid syntax
>>> a[1:}
	  
SyntaxError: invalid syntax
>>> a[1:]
	  
'agen Sakam Bhim Soren '
>>> a[4:]
	  
'n Sakam Bhim Soren '
>>> a[:5]
	  
'Sagen'
>>> a[-1]
	  
' '
>>> a[:: -1]
	  
' neroS mihB makaS negaS'
>>> ############ Properties
	  
>>> s
	  
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    s
NameError: name 's' is not defined
>>> s
	  
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    s
NameError: name 's' is not defined
>>> a
	  
'Sagen Sakam Bhim Soren '
>>> a[0] = s
	  
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    a[0] = s
NameError: name 's' is not defined
>>> a[0] = 's'
	  
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    a[0] = 's'
TypeError: 'str' object does not support item assignment
>>> a[1] = 'a'
	  
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    a[1] = 'a'
TypeError: 'str' object does not support item assignment
>>> a
	  
'Sagen Sakam Bhim Soren '
>>> ###### Concatenate
	  
>>> b = 'Ghatsila'
	  
>>> c = a + b
	  
>>> c
	  
'Sagen Sakam Bhim Soren Ghatsila'
>>> letter = 'S'
	  
>>> letter * 10
	  
'SSSSSSSSSS'
>>> a.upper()
	  
'SAGEN SAKAM BHIM SOREN '
>>> a.lower()
	  
'sagen sakam bhim soren '
>>> a.split()
	  
['Sagen', 'Sakam', 'Bhim', 'Soren']
>>> a.split('b')
	  
['Sagen Sakam Bhim Soren ']
>>> a.split('B')
	  
['Sagen Sakam ', 'him Soren ']
>>> 
