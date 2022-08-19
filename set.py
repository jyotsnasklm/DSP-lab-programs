Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> s1={1,2,3}
>>> type(s1)
<class 'set'>
>>> s2={3,4,5}
>>> print(s1)
{1, 2, 3}
>>> print(s2)
{3, 4, 5}
>>> s1.union(s2)
{1, 2, 3, 4, 5}
>>> s1.insertion(s2)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    s1.insertion(s2)
AttributeError: 'set' object has no attribute 'insertion'
>>> help(s1)
Help on set object:

class set(object)
 |  set() -> new empty set object
 |  set(iterable) -> new set object
 |  
 |  Build an unordered collection of unique elements.
 |  
 |  Methods defined here:
 |  
 |  __and__(self, value, /)
 |      Return self&value.
 |  
 |  __contains__(...)
 |      x.__contains__(y) <==> y in x.
 |  
 |  __eq__(self, value, /)
 |      Return self==value.
 |  
 |  __ge__(self, value, /)
 |      Return self>=value.
 |  
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |  
 |  __gt__(self, value, /)
 |      Return self>value.
 |  
 |  __iand__(self, value, /)
 |      Return self&=value.
 |  
 |  __init__(self, /, *args, **kwargs)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |  
 |  __ior__(self, value, /)
 |      Return self|=value.
 |  
 |  __isub__(self, value, /)
 |      Return self-=value.
 |  
 |  __iter__(self, /)
 |      Implement iter(self).
 |  
 |  __ixor__(self, value, /)
 |      Return self^=value.
 |  
 |  __le__(self, value, /)
 |      Return self<=value.
 |  
 |  __len__(self, /)
 |      Return len(self).
 |  
 |  __lt__(self, value, /)
 |      Return self<value.
 |  
 |  __ne__(self, value, /)
 |      Return self!=value.
 |  
 |  __or__(self, value, /)
 |      Return self|value.
 |  
 |  __rand__(self, value, /)
 |      Return value&self.
 |  
 |  __reduce__(...)
 |      Return state information for pickling.
 |  
 |  __repr__(self, /)
 |      Return repr(self).
 |  
 |  __ror__(self, value, /)
 |      Return value|self.
 |  
 |  __rsub__(self, value, /)
 |      Return value-self.
 |  
 |  __rxor__(self, value, /)
 |      Return value^self.
 |  
 |  __sizeof__(...)
 |      S.__sizeof__() -> size of S in memory, in bytes
 |  
 |  __sub__(self, value, /)
 |      Return self-value.
 |  
 |  __xor__(self, value, /)
 |      Return self^value.
 |  
 |  add(...)
 |      Add an element to a set.
 |      
 |      This has no effect if the element is already present.
 |  
 |  clear(...)
 |      Remove all elements from this set.
 |  
 |  copy(...)
 |      Return a shallow copy of a set.
 |  
 |  difference(...)
 |      Return the difference of two or more sets as a new set.
 |      
 |      (i.e. all elements that are in this set but not the others.)
 |  
 |  difference_update(...)
 |      Remove all elements of another set from this set.
 |  
 |  discard(...)
 |      Remove an element from a set if it is a member.
 |      
 |      If the element is not a member, do nothing.
 |  
 |  intersection(...)
 |      Return the intersection of two sets as a new set.
 |      
 |      (i.e. all elements that are in both sets.)
 |  
 |  intersection_update(...)
 |      Update a set with the intersection of itself and another.
 |  
 |  isdisjoint(...)
 |      Return True if two sets have a null intersection.
 |  
 |  issubset(...)
 |      Report whether another set contains this set.
 |  
 |  issuperset(...)
 |      Report whether this set contains another set.
 |  
 |  pop(...)
 |      Remove and return an arbitrary set element.
 |      Raises KeyError if the set is empty.
 |  
 |  remove(...)
 |      Remove an element from a set; it must be a member.
 |      
 |      If the element is not a member, raise a KeyError.
 |  
 |  symmetric_difference(...)
 |      Return the symmetric difference of two sets as a new set.
 |      
 |      (i.e. all elements that are in exactly one of the sets.)
 |  
 |  symmetric_difference_update(...)
 |      Update a set with the symmetric difference of itself and another.
 |  
 |  union(...)
 |      Return the union of sets as a new set.
 |      
 |      (i.e. all elements that are in either set.)
 |  
 |  update(...)
 |      Update a set with the union of itself and others.
 |  
 |  ----------------------------------------------------------------------
 |  Class methods defined here:
 |  
 |  __class_getitem__(...) from builtins.type
 |      See PEP 585
 |  
 |  ----------------------------------------------------------------------
 |  Static methods defined here:
 |  
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.
 |  
 |  ----------------------------------------------------------------------
 |  Data and other attributes defined here:
 |  
 |  __hash__ = None

>>> s1.union(s2)
{1, 2, 3, 4, 5}
>>> s1.insection(s2)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    s1.insection(s2)
AttributeError: 'set' object has no attribute 'insection'
>>> s1.intersection(s2)
{3}
>>> s1.difference(s2)
{1, 2}
>>> s1.issubset(s2)
False
>>> s1.difference_update(s2)
>>> print(s1)
{1, 2}
>>> s1.update(s2)
>>> print(s1)
{1, 2, 3, 4, 5}
>>> s2.difference(s1)
set()
>>> print(s2)
{3, 4, 5}
>>> s1.isdisjoint(s2)
False
>>> s3={6,7,8}
>>> s1.isdisjoint(s3)
True
>>> s3.isdisjoint(s2)
True
>>> s1.discard(s2)
>>> print(s1)
{1, 2, 3, 4, 5}
>>> print(s2)
{3, 4, 5}
>>> s1.copy()
{1, 2, 3, 4, 5}
>>> s1={1,2,3}
>>> s1.copy()
{1, 2, 3}
>>> s2={3,4,5}
>>> print(s1)
{1, 2, 3}
>>> print(s2)
{3, 4, 5}
>>> s1.discard(s2)
>>> print(s1)
{1, 2, 3}
>>> print(s2)
{3, 4, 5}
>>> s2.copy()
{3, 4, 5}
>>> s3.pop()
8
>>> print(s3)
{6, 7}
>>> s3.pop(s3)
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    s3.pop(s3)
TypeError: set.pop() takes no arguments (1 given)
>>> s3.pop()
6
>>> print(s3)
{7}
>>> s3=(10.20,30)
>>> s3=(10,20,30)
>>> s3.remove(2)
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    s3.remove(2)
AttributeError: 'tuple' object has no attribute 'remove'
>>> s3.remove(20)
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    s3.remove(20)
AttributeError: 'tuple' object has no attribute 'remove'
>>> s={1,2,3,4,5}
>>> print(s)
{1, 2, 3, 4, 5}
>>> s.remove(4)
>>> print(s)
{1, 2, 3, 5}
>>> s.pop()
1
>>> print(s)
{2, 3, 5}
>>> 