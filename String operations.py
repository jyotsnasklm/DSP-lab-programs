Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> s1="python"
>>> s1
'python'
>>> print(s1)
python
>>> type(s1)
<class 'str'>
>>> len(s1)
6
>>> print(len(s1))
6
>>> s1.capitalize
<built-in method capitalize of str object at 0x000001CE32A247B0>
>>> s1.upper()
'PYTHON'
>>> s1.lower()
'python'
>>> s1.islower()
True
>>> s1.isupper()
False
>>> s1.capitalize()
'Python'
>>> s1.isalpha()
True
>>> s1.isdigit()
False
>>> s1.isnumeric()
False
>>> s1.isspace()
False
>>> s1.istitle()
False
>>> max(s1)
'y'
>>> min(s1)
'h'
>>> s1.swapcase()
'PYTHON'
>>> s1.isdecimal()
False
>>> s=s180850
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    s=s180850
NameError: name 's180850' is not defined
>>> s1="jyotsna"
>>> s1
'jyotsna'
>>> s2="s180850"
>>> s2
's180850'
>>> s1.upper()
'JYOTSNA'
>>> s2.upper()
'S180850'
>>> s1.lower()
'jyotsna'
>>> s2.lower()
's180850'
>>> s1=s2
>>> s3=s1
>>> s1
's180850'
>>> s2
's180850'
>>> s3
's180850'
>>> s1.isupper()
False
>>> s1.islower()
True
>>> s1.capitalize()
'S180850'
>>> max(s2)
's'
>>> min(s2)
'0'
>>> max(s1)
's'
>>> len(s1)
7
>>> s2.isnumeric()
False
>>> s2.rstrip()
's180850'
>>> s1.istitle()
False
>>> s2.find("s")
0
>>> s2.zfill(4)
's180850'
>>> s2.zfill(0)
's180850'
>>> 
