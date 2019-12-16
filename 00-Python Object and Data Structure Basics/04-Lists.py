Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
#########################################################33
>>> ####  LISTS
>>> ######################################################
>>> my_list = [1,2,3,4]
>>> len(my_list)
4
>>> my_list.append('Sagen')
>>> my_list
[1, 2, 3, 4, 'Sagen']
>>> my_list.pop(5)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    my_list.pop(5)
IndexError: pop index out of range
>>> my_list.pop(4)
'Sagen'
>>> my_list()
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    my_list()
TypeError: 'list' object is not callable
>>> my_list
[1, 2, 3, 4]
>>> my_list.reverse()
>>> my_list
[4, 3, 2, 1]
>>> my_list.sort()
>>> my_list
[1, 2, 3, 4]
>>> my_list1 = [5,6,7,8]
>>> my_list2 = [9,10,11,12]
>>> martix = [my_list, my_list1,my_list2]
>>> matrix = martix
>>> matrix
[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
>>> matrix[0,1]
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    matrix[0,1]
TypeError: list indices must be integers or slices, not tuple
>>> matrix[0]
[1, 2, 3, 4]
>>> matrix[0][0]
1
>>> matrix[1][3]
8
>>> 
>>> first_col = [row[0] for row in matrix]
>>> first_col
[1, 5, 9]
>>> second_col = [row[1] for row in matrix]
>>> second_col
[2, 6, 10]
>>> third_col = [row[2] for row in matrix]
>>> third_col
[3, 7, 11]
>>> fourth_col = [row[3] for row in matrix]
>>> fourth_col
[4, 8, 12]
>>> first_row = [col[0] for col in matrix]
>>> first_row
[1, 5, 9]
>>> 
