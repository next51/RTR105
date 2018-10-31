Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:22:17) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> str = "Hello"
>>> Type "copyright", "credits" or "license()" for more information.str = "Hello"Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:22:17) [MSC v.1500 32 bit (Intel)] on win32
SyntaxError: invalid syntax
>>> str = "Hello"
>>> str1 = "Hello"
>>> str2 = 'there'
>>> bob = str1 + str2
>>> print(bob)
Hellothere
>>> str3 = '123'
>>> str3 = str3 + 1

Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    str3 = str3 + 1
TypeError: cannot concatenate 'str' and 'int' objects
>>> type(str3)
<type 'str'>
>>> type(1_)
SyntaxError: invalid syntax
>>> type(1)
<type 'int'>
>>> x = int(str3) + 1
>>> print(x)
124
>>> name = input('Enter)
	     
SyntaxError: EOL while scanning string literal
>>> name = input('Enter')
Enter Chuck

Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    name = input('Enter')
  File "<string>", line 1, in <module>
NameError: name 'Chuck' is not defined
>>> 
=================== RESTART: C:/Users/Makson/Desktop/2.py ===================
Enter: Chuck

Traceback (most recent call last):
  File "C:/Users/Makson/Desktop/2.py", line 1, in <module>
    name = input('Enter')
  File "<string>", line 1
    : Chuck
    ^
SyntaxError: invalid syntax
>>> 
=================== RESTART: C:/Users/Makson/Desktop/2.py ===================
Enter Chuck

Traceback (most recent call last):
  File "C:/Users/Makson/Desktop/2.py", line 1, in <module>
    name = input('Enter')
  File "<string>", line 1, in <module>
NameError: name 'Chuck' is not defined
>>> 
=================== RESTART: C:/Users/Makson/Desktop/2.py ===================
Enter:3

Traceback (most recent call last):
  File "C:/Users/Makson/Desktop/2.py", line 1, in <module>
    name = input('Enter:')
  File "<string>", line 0
    
    ^
SyntaxError: unexpected EOF while parsing
>>> 
=================== RESTART: C:/Users/Makson/Desktop/2.py ===================
Enter:Chuck

Traceback (most recent call last):
  File "C:/Users/Makson/Desktop/2.py", line 1, in <module>
    name = input('Enter:')
  File "<string>", line 1, in <module>
NameError: name 'Chuck' is not defined
>>> fruit = 'bannana'
>>> letter = fruit[1]
>>> print(letter)
a
>>> x = 3
>>> w = fruit[x-1]
>>> print(w)
n
>>> fruit = 'bannana'
>>> print(len(fruit))
7
>>> fruit = 'banana'
>>> for letter in fruit:
	print(letter)

	
b
a
n
a
n
a
>>> fruit = 'banana'
>>> for letter in fruit:
	print(letter)

	
b
a
n
a
n
a
>>> index = 0
>>> while index < len(fruit):
	letter = fruit[index]
	print(letter)
	index = index + 1

	
b
a
n
a
n
a
>>> word = 'banana'
>>> count = 0
>>> for letter in word:
	if letter == 'a':
		count = count + 1
	print(count)

	
0
1
1
2
2
3
>>> s = 'Monty Python'
>>> print (s[0:4])
Mont
>>> print(s[6:7])
P
>>> print(s[6:20])
Python
>>> print(s[6:11])
Pytho
>>> print(s[6:12])
Python
>>> print(s[:2])
Mo
>>> print(s[8:])
thon
>>> print(s[:])
Monty Python
>>> s
'Monty Python'
>>> print(s)
Monty Python
>>> a = 'Hello'
>>> b = a +'There'
>>> print(b)
HelloThere
>>> c = a + '' + 'There'
>>> print(c)
HelloThere
>>> c = a + '' + 'There'
>>> 
>>> c
'HelloThere'
>>> c = a + ' ' + 'There'
>>> c
'Hello There'
>>> c = a + ' ' + 'There'
>>> c
'Hello There'
>>> fruit = 'banana'
>>> 'n' in fruit
True
>>> 'm' in fruit
False
>>> nan in ruit

Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    nan in ruit
NameError: name 'nan' is not defined
>>> 'nan' in ruit

Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    'nan' in ruit
NameError: name 'ruit' is not defined
>>> 'nan' in fruit
True
>>> if 'a' in fruit:
	print('Found it')

	
Found it
>>> 
=================== RESTART: C:/Users/Makson/Desktop/3.py ===================

Traceback (most recent call last):
  File "C:/Users/Makson/Desktop/3.py", line 1, in <module>
    if word == 'banana':
NameError: name 'word' is not defined
>>> 
=================== RESTART: C:/Users/Makson/Desktop/3.py ===================

Traceback (most recent call last):
  File "C:/Users/Makson/Desktop/3.py", line 2, in <module>
    if word == 'banana':
NameError: name 'word' is not defined
>>> greet = 'Hello Bob'
>>> zap = greet.lower()
>>> print(zap)
hello bob
>>> print(greet)
Hello Bob
>>> stuff = 'Hello world'
>>> type(stuff)
<type 'str'>
>>> dir(stuff)
['__add__', '__class__', '__contains__', '__delattr__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getslice__', '__gt__', '__hash__', '__init__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '_formatter_field_name_split', '_formatter_parser', 'capitalize', 'center', 'count', 'decode', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'index', 'isalnum', 'isalpha', 'isdigit', 'islower', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> fruit = 'banana'
>>> pos = fruit.find('na')
>>> print(pos)
2
>>> aa = fruit.find('z')
>>> print(aa)
-1
>>> greet = 'Hello bob'
>>> nnn = greet.upper()
>>> print(nnn)
HELLO BOB
>>> www = greet.lower()
>>> print(wwww)

Traceback (most recent call last):
  File "<pyshell#95>", line 1, in <module>
    print(wwww)
NameError: name 'wwww' is not defined
>>> print(www)
hello bob
>>> greet = 'Hello Bob'
>>> nstr = greet.replace('Bob','Jane')
>>> print(nstr)
Hello Jane
>>> nstr = greet.replace('o','X')
>>> print(nstr)
HellX BXb
>>> greet = 'Hello Bob'
>>> print(greet)
Hello Bob
>>> greet = ' Hello Bob '
>>> print(greet)
 Hello Bob 
>>> nsrt = greet.lstrip()
>>> print(nstr)
HellX BXb
>>> greet = ' Hello Bob '
>>> greet.lstrip()
'Hello Bob '
>>> greet.rstrip()
' Hello Bob'
>>> greet.strip()
'Hello Bob'
>>> line = 'Please have a nice day'
>>> line.startswith('Please')
True
>>> line.startswith('p')
False
>>> line.startswith('P')
True
>>> line.endswith('P')
False
>>> line.endswith('y')
True
>>> data = 'From stephen.marquard@uct.az.za Sat Jan 5 09:14:16 2008'
>>> aptos = data.find('@')
>>> print(atpos)

Traceback (most recent call last):
  File "<pyshell#120>", line 1, in <module>
    print(atpos)
NameError: name 'atpos' is not defined
>>> aptos = data.find('a')
>>> print(atpos)

Traceback (most recent call last):
  File "<pyshell#122>", line 1, in <module>
    print(atpos)
NameError: name 'atpos' is not defined
>>> 
