Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> s="jyotsna"
>>> s.capitalize()
'Jyotsna'
>>> s.upper()
'JYOTSNA'
>>> s.lower()
'jyotsna'
>>> s.isupper()
False
>>> s.islower()
True
>>> s.len()
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    s.len()
AttributeError: 'str' object has no attribute 'len'
>>> len()
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    len()
TypeError: len() takes exactly one argument (0 given)
>>> len(s)
7
>>> max(s)
'y'
>>> min(s)
'a'
>>> s.isdigit()
False
>>> s.isalphnum()
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    s.isalphnum()
AttributeError: 'str' object has no attribute 'isalphnum'
>>> s.isnum()
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    s.isnum()
AttributeError: 'str' object has no attribute 'isnum'
>>> s.swapcase()
'JYOTSNA'
>>> s.title()
'Jyotsna'
>>> s.strip()
'jyotsna'
>>> s.index()
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    s.index()
TypeError: index() takes at least 1 argument (0 given)
>>> 