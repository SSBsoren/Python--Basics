Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> file1 = open("MyFile.txt","a")
>>> file1
<_io.TextIOWrapper name='MyFile.txt' mode='a' encoding='cp1252'>
>>> pwd
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    pwd
NameError: name 'pwd' is not defined
>>> #### Opening a file
>>> file_object  = open(r"File_Name", "Access_Mode")
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    file_object  = open(r"File_Name", "Access_Mode")
ValueError: invalid mode: 'Access_Mode'
>>> file1
<_io.TextIOWrapper name='MyFile.txt' mode='a' encoding='cp1252'>
>>> file2 = open("My_file.text","w")
>>> L = [ "This is first Line
	  
SyntaxError: EOL while scanning string literal
>>> L = [ " This is first Line "\n, "This is second Line "\n" ,"This is third line "\n]
	  
SyntaxError: unexpected character after line continuation character
>>> L = [ " This is first Line "\n, "This is second Line "\n" ,"This is third line "\n]
	  
SyntaxError: unexpected character after line continuation character
>>> L = [ " This is first Line "\n, "This is second Line "\n" ,"This is third line \n "]
	  
SyntaxError: unexpected character after line continuation character
>>> L = [ " This is first Line \n", "This is second Line \n" ,"This is third line \n"]
	  
>>> l
	  
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    l
NameError: name 'l' is not defined
>>> file2
	  
<_io.TextIOWrapper name='My_file.text' mode='w' encoding='cp1252'>
>>> file2.write("Hello \n")
	  
7
>>> file2 = open("My_file.txt","r+")
	  
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    file2 = open("My_file.txt","r+")
FileNotFoundError: [Errno 2] No such file or directory: 'My_file.txt'
>>> file2 = open("My_file.text","r+")
	  
>>> print file.read()
	  
SyntaxError: invalid syntax
>>> print file2.read()
	  
SyntaxError: invalid syntax
>>> print file2.read()
	  
SyntaxError: invalid syntax
>>> 
