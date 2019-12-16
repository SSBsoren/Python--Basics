Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
my_dict = {'key1' : value1, 'key2' : value2,'key3' : value3}
Traceback (most recent call last):
  File "<pyshell#0>", line 2, in <module>
    my_dict = {'key1' : value1, 'key2' : value2,'key3' : value3}
NameError: name 'value1' is not defined
>>> my_dict = {'key1' : 'value1', 'key2' : 'value2','key3' :' value3'}
>>> my_dick
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    my_dick
NameError: name 'my_dick' is not defined
>>> my_dict
{'key1': 'value1', 'key2': 'value2', 'key3': ' value3'}
>>> my_dict['key2']
'value2'
>>> my_dict['key4'] = 'value4'
>>> my_dict
{'key1': 'value1', 'key2': 'value2', 'key3': ' value3', 'key4': 'value4'}
>>> my_dict['key5'] = ['value5',1,2,3,'four','six']
>>> my_dict
{'key1': 'value1', 'key2': 'value2', 'key3': ' value3', 'key4': 'value4', 'key5': ['value5', 1, 2, 3, 'four', 'six']}
>>> my_nested_dict = {my_dict,'key6': 'key',
		      
SyntaxError: invalid syntax
>>> my_nested_dict = {my_dict,'key6': 'key']
		      
SyntaxError: invalid syntax
>>> a_dict = {'key' : {'nestkey' : {'subnestkey' : 'value'}}}
		      
>>> a_dict
		      
{'key': {'nestkey': {'subnestkey': 'value'}}}
>>> my_dict.keys()
		      
dict_keys(['key1', 'key2', 'key3', 'key4', 'key5'])
>>> my_dict.values()
		      
dict_values(['value1', 'value2', ' value3', 'value4', ['value5', 1, 2, 3, 'four', 'six']])
>>> my_dict.items()
		      
dict_items([('key1', 'value1'), ('key2', 'value2'), ('key3', ' value3'), ('key4', 'value4'), ('key5', ['value5', 1, 2, 3, 'four', 'six'])])
>>> 
