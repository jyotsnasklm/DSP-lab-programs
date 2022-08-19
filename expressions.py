Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a,b=10,20
>>> print(a)
10
>>> print(b)
20
>>> a=10,b=20
SyntaxError: cannot assign to literal
>>> a=10
>>> b=20
>>> c=a=b
>>> print(c)
20
>>> c=a+b
>>> print(c)
40
>>> a=10
>>> b=20
>>> c=a-b
>>> print(c)
-10
>>> c=a+b
>>> print(c)
30
>>> a=10
>>> b=20
>>> c=a>b
>>> print(c)
False
>>> c=a<b
>>> print(c)
True
>>> a=10
>>> type(a)
<class 'int'>
>>> a=10
>>> b=20
>>> c=a<b
>>> type(c)
<class 'bool'>
>>> a=10
>>> float(a)
10.0
>>> a=20.5
>>> int(a)
20
>>> x="jyotsna"
>>> print(x)
jyotsna
>>> type(x)
<class 'str'>
>>> type(a)
<class 'float'>
>>> len(x)
7
>>> a++
SyntaxError: invalid syntax
>>> x="jyotsna"
x.capitalize()

