Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:22:17) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def thing():
	print('Hello')
	print('Fun')

	
>>> thing()
Hello
Fun
>>> print('Zip')
Zip
>>> thing()
Hello
Fun
>>> big = max('Hello world')
>>> print(big)
w
>>> tiny = min('Hello world')
>>> print(tiny)
 
>>> type(x)

Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    type(x)
NameError: name 'x' is not defined
>>> type(w)

Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    type(w)
NameError: name 'w' is not defined
>>> type(123)
<type 'int'>
>>> x = 123
>>> type(x)
<type 'int'>
>>> print(float(99)/100)
0.99
>>> i = 42
>>> type(i)
<type 'int'>
>>> f = float(i)
>>> print(f)
42.0
>>> type(f)
<type 'float'>
>>> print(1+2*floay(3)/4-5)

Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    print(1+2*floay(3)/4-5)
NameError: name 'floay' is not defined
>>> print(1+2*float(3)/4-5)
-2.5
>>> def print_lyrics():
	print("I'm a lumberjack, and I'm okay.")
	print('I sleep all night and I work all day.')

	
>>> x = 5
>>> print('Hello')
Hello
>>> def print_lyrics():
	print("I'm lumberjacks and I'm okay.")
	print('I sleep all night and I work all day.')
    print('Yo')
    
  File "<pyshell#37>", line 5
    print('Yo')
              ^
IndentationError: unindent does not match any outer indentation level
>>> print('Yo')
Yo
>>> x = x+2
>>> print(x)
7
>>> x = 5
>>> print('Hello')
Hello
>>> def print_lyrics():
	print("I'm a lumberjack, and I'm okay.")
	print('I sleep all night and work all day.')
	print('Yo')
	print_lyrics()
	x = x + 2
	print(x)

	
>>> 
>>> 
================= RESTART: C:/Users/Makson/Desktop/323232.py =================
Hello
Yo
I'm a lumberjack, and I'm okay.
I sleep all night and I work all day.
7
>>> def greet(lang):
	if lang == 'es':
		print('Hola')
	elif lang == 'ft':
		print('Bonjour')
	else:
		print('Hello')

		
>>> greet('en')
Hello
>>> greet('es')
Hola
>>> greet('fr')
Hello
>>> greet('ft')
Bonjour
>>> greet('rus')
Hello
>>> def greet():
	return "Hello"

>>> print(greet(), "Glenn")
('Hello', 'Glenn')
>>> print(greet(), "Sally")
('Hello', 'Sally')
>>> def greet(lang):
	if lang == 'es':
		return 'Hola'
	elif lang == 'fr':
		return 'Bonjour'
	else:
		return 'Hello'

	
>>> print(greet('en'), 'Gleen')
('Hello', 'Gleen')
>>> print(greet('es') 'Sally')
SyntaxError: invalid syntax
>>> print(greet('es'), 'Sally')
('Hola', 'Sally')
>>> print(greet('fr'), 'Michael')
('Bonjour', 'Michael')
>>> def addtwo(a,b):
	added = a + b
	return added

>>> x = addtwo(3,5)
>>> print(x)
8
>>> 
