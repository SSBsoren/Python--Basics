Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #String formatting
>>> player = 'Sagen'
>>> points = 143
>>> print( "Last night,' + player + ' +str(points) +' points.")
Last night,' + player + ' +str(points) +' points.
>>> ' last night , '+player '
SyntaxError: EOL while scanning string literal
>>> 'Last night, '+player+' scored '+str(points)+' points.'
'Last night, Sagen scored 143 points.'
>>> f'last night, {player} scored {points} points.'
'last night, Sagen scored 143 points.'
>>> #######################################################
>>> ### formatting with plaeeholders
>>> ######################################################
>>> print(" I'am %s Soren." %'Sagen')
 I'am Sagen Soren.
>>> print(" I'm %s Soren from %s." %('Sagen ','Jamshedpur'))
 I'm Sagen  Soren from Jamshedpur.
>>> 
>>> x,y = 'Sagen','Soren'
>>> print('This is %s %s.'%(x,y))
This is Sagen Soren.
>>> ##################################################3
>>> ##### Format Converstion methods
>>> ###################################################
>>> print("I'm %s."%'Sagen
	  
SyntaxError: EOL while scanning string literal
>>> print("I'm %s."%'Sagen')
	  
I'm Sagen.
>>> print("I'm %r."%'Sagen')
	  
I'm 'Sagen'.
>>> print("I once caught a fish %s.' %'this
	  
SyntaxError: EOL while scanning string literal
>>> print('I once caught a fish %s.'this\tbig')
	  
SyntaxError: invalid syntax
>>> print('I once caught a fish %s.'%'this \tbig')
	  
I once caught a fish this 	big.
>>> >>> print('I once caught a fish %r.'%'this \tbig')
	  
SyntaxError: invalid syntax
>>> >>> print('I once caught a fish %r.'%'this \tbig')
	  
SyntaxError: invalid syntax
>>> print('I once caught a fish %r.' %'this \tbig')
	  
I once caught a fish 'this \tbig'.
>>> print('I wrote %s Programs today.' %'4.55)
	  
SyntaxError: EOL while scanning string literal
>>> print('value is %s.' %'5.44')
	  
value is 5.44.
>>> print('Value is %d.' %'5.55')
	  
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    print('Value is %d.' %'5.55')
TypeError: %d format: a number is required, not str
>>> print('Value is %d.'%5.44')
	  
SyntaxError: EOL while scanning string literal
>>> print('Value is %d.' %5.55)
	  
Value is 5.
>>> #################################################3
	  
>>> #### Padding and Precision of floating Points Numbers
	  
>>> ########################################################
	  
>>> print('floating point no : %5.4f' %(13.144))
	  
floating point no : 13.1440
>>> print('Floating points no : %2.2f' %(1222.4452))
	  
Floating points no : 1222.45
>>> print('Floating points no : %5.3f' %(13453.32455))
	  
Floating points no : 13453.325
>>>  print('Floating points no : %5.3f' %(134533.32455))
	  
SyntaxError: unexpected indent
>>> print('Floating points no : %5.3f' %(133453.32455))
	  
Floating points no : 133453.325
>>>  print('Floating points no : %5.3f' %(153.32455))
	  
SyntaxError: unexpected indent
>>> print('Floating points no : %5.3f' %(133.32455))
	  
Floating points no : 133.325
>>> print('Floating points no : %1.0f' %(13453.32455))
	  
Floating points no : 13453
>>> print('Floating points no : %5.3f' %(133.5))
	  
Floating points no : 133.500
>>> ##################################################3
	  
>>> ####### Multiple Formatting
	  
>>> ##################################################
	  
>>> print('First: %s, Second  :%5.2f, third: %r ' %('Sagen', 160.166,'Soren'))
	  
First: Sagen, Second  :160.17, third: 'Soren' 
>>> ##################### Formatting with the .formate() method
	  
>>> print('This is a string with an  {} '.format('insert'))
	  
This is a string with an  insert 
>>> print('Hi! this is {} {} {} {}'/format('Sagen','Sakam','Bhim','Soren'))
	  
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    print('Hi! this is {} {} {} {}'/format('Sagen','Sakam','Bhim','Soren'))
TypeError: format() takes at most 2 arguments (4 given)
>>> print('Hi! this is {} {} {} {}'.format('Sagen','Sakam','Bhim','Soren'))
	  
Hi! this is Sagen Sakam Bhim Soren
>>> print('Hi! this is {2} {1} {0 {}'/format('Sagen','Sakam','Bhim','Soren'))
	  
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    print('Hi! this is {2} {1} {0 {}'/format('Sagen','Sakam','Bhim','Soren'))
TypeError: format() takes at most 2 arguments (4 given)
>>> print('Hi! this is {2} {1} {0} {3}'/format('Sagen','Sakam','Bhim','Soren'))
	  
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    print('Hi! this is {2} {1} {0} {3}'/format('Sagen','Sakam','Bhim','Soren'))
TypeError: format() takes at most 2 arguments (4 given)
>>> print('Hi! this is {2} {1} {0} {3}'.format('Sagen','Sakam','Bhim','Soren'))
	  
Hi! this is Bhim Sakam Sagen Soren
>>> print('Hi! this is middleName:{2} middleName:{1} FirstName:{0} LastName:{3}'.format('Sagen','Sakam','Bhim','Soren'))
	  
Hi! this is middleName:Bhim middleName:Sakam FirstName:Sagen LastName:Soren
>>> print(' FirstName : %s and NickName : %s '%('Sagen','Sagen'))
	  
 FirstName : Sagen and NickName : Sagen 
>>> print('Firstname : {s} and NickName :{s}'.format(p = 'Sagen'))
	  
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    print('Firstname : {s} and NickName :{s}'.format(p = 'Sagen'))
KeyError: 's'
>>> print('Firstname : {s} and NickName :{s}'.format(s = 'Sagen'))
	  
Firstname : Sagen and NickName :Sagen
>>> #################################################################################
	  
>>> ### Alignment, padding and precision with .format()
	  
>>> #################################################################################
	  
>>> print('{0:8} | {1:9}'.format('Sagen','Soren'))
	  
Sagen    | Soren    
>>> print('{0:8} | {1:9}'.format('Parwati','Soren'))
	  
Parwati  | Soren    
>>> print('{0:8} | {1:9}'.format('Shalni','Soren'))
	  
Shalni   | Soren    
>>> print('{0:<8} | {1:^8} | {2:>8}'.format('Left','center','right'))
	  
Left     |  center  |    right
>>> print('{0:<8} | {1:^8} | {2:>8}'.format('120','190','122'))
	  
120      |   190    |      122
>>> print('{0:=<8} | {1:-^8} | {2:.>8}'.format('222','333','444'))
	  
222===== | --333--- | .....444
>>> print('the obtained mark in percentage : %10.2f ' %56.23111)
	  
the obtained mark in percentage :      56.23 
>>> print('the obtained mark in percentage : {0:10.2f} ' .format(56.23111))
	  
the obtained mark in percentage :      56.23 
>>> ##########################################################################3
	  
>>> ######## Formatting String with Literals (f-string)
	  
>>> ###########################################################################
	  
>>> 
	  
>>> name = 'Sagen';print(f"HE SAID HIS NAME IS {name}.")
	  
HE SAID HIS NAME IS Sagen.
>>> print(f" He said his name is {name!r}")
	  
 He said his name is 'Sagen'
>>> num = 166.1601229166
	  
>>> print(" My 6 character, four decimal number is : {0:6.4f}".format(num))
	  
 My 6 character, four decimal number is : 166.1601
>>> My 10 character, four decimal number is : 166.1601
	  
SyntaxError: invalid syntax
>>> print(" My 10 character, four decimal number is : {num:{10}.{6}}")
	  
 My 10 character, four decimal number is : {num:{10}.{6}}
>>> print(f" My 10 character, four decimal number is : {num:{10}.{6}}")
	  
 My 10 character, four decimal number is :     166.16
>>> #############For more info on formatted string literals visit https://docs.python.org/3/reference/lexical_analysis.html#f-strings
