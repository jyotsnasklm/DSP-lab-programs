Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> L=[]
>>> print(type(L))
<class 'list'>
>>> help(L)

>>> x=[1,2,3,4,5,6]
>>> print(X)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    print(X)
NameError: name 'X' is not defined
>>> print(x);
[1, 2, 3, 4, 5, 6]
>>> x=x+[7,8,9]
>>> print(x);
[1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> x[-1]=200
>>> print(x);
[1, 2, 3, 4, 5, 6, 7, 8, 200]
>>> x[1:3]=[111,222,333]
>>> print(x);
[1, 111, 222, 333, 4, 5, 6, 7, 8, 200]
>>> len(x)
10
>>> x.ext
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    x.ext
AttributeError: 'list' object has no attribute 'ext'
>>> x
[1, 111, 222, 333, 4, 5, 6, 7, 8, 200]
>>> x.extend(111,222,333)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    x.extend(111,222,333)
TypeError: list.extend() takes exactly one argument (3 given)
>>> 