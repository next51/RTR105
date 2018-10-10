Python 2.7.12 (default, Dec  4 2017, 14:50:18) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> print(123)
123
>>> print(98.6)
98.6
>>> print('Hello world')
Hello world
>>> variable

Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    variable
NameError: name 'variable' is not defined
>>> variable "x"
SyntaxError: invalid syntax
>>> "mnemonic = memory aid
SyntaxError: EOL while scanning string literal
>>> "mnemonic" = "memory aid"
SyntaxError: can't assign to literal
>>> x1q3zocd = 35.0
>>> x1q3zocd = 12.50
>>> x1q3zocd = x1q3zocd * x1q3zocd
>>> print(x1q3zocd)
156.25
>>> hours = 35.0
>>> rate = 12.50
>>> pay = hours*rate
>>> print(pay)
437.5
>>> a = 5538
>>> b = 1000
>>> c = a / b
>>> print(c)
5
>>> print = 5538
SyntaxError: invalid syntax
>>> a = 5538.0
>>> b = 1000.0
>>> c = a / b
>>> print(c)
5.538
>>> x = 2
>>> x = x+2
>>> print(x)
4
>>> x = 3.9*x*(1-x)
>>> print(x)
-46.8
>>> xx=2
>>> xx=xx+2
>>> print(xx)
4
>>> yy=440*12
>>> print(yy)
5280
>>> zz=yy/1000
>>> print(zz)
5
>>> zz = yy / 1000
>>> print(zz)
5
>>> jj = 23
>>> kk = jj % 5
>>> print(kk)
3
>>> print(4**3)
64
>>> x=1+2**3/4*5
>>> print(x)
11
>>> ddd=1+4
>>> print(ddd)
5
>>> eee='hello'+'there'
>>> print(eee)
hellothere
>>> eee='hello'+ 'there'
>>> print(eee)
hellothere
>>> type 'float'
SyntaxError: invalid syntax
>>> type float
SyntaxError: invalid syntax
>>> <type 'float'>
SyntaxError: invalid syntax
>>> a = 4
>>> b = 3
>>> c = a % b
>>> c
1
>>> a = 4
>>> c = a % b
>>> c
1
>>> a = 4.
>>> c = a % b
>>> c
1.0
>>> a = 999
>>> b = 1000
>>> c = a % b
>>> c
999
>>> xx=1
>>> type(xx)
<type 'int'>
>>> <class 'int'>
SyntaxError: invalid syntax
>>> xx=1
>>> type(xx)
<type 'int'>
>>> y=98.6
>>> type(y)
<type 'float'>
>>> print(float(99)+100)
199.0
>>> i = 42
>>> type(i)
<type 'int'>
>>> f=(floati)

Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    f=(floati)
NameError: name 'floati' is not defined
>>> f=float(i)
>>> print(f)
42.0
>>> type(f)
<type 'float'>
>>> print(10/2)
5
>>> print(9/2)
4
>>> print(99/100)
0
>>> print(10.0/2.0)
5.0
>>> print(99.0/100.0)
0.99
>>> sval='123'
>>> type(sval)
<type 'str'>
>>> print(sval+1)

Traceback (most recent call last):
  File "<pyshell#89>", line 1, in <module>
    print(sval+1)
TypeError: cannot concatenate 'str' and 'int' objects
>>> print(sval + 1)

Traceback (most recent call last):
  File "<pyshell#90>", line 1, in <module>
    print(sval + 1)
TypeError: cannot concatenate 'str' and 'int' objects
>>> inval = int(sval)
>>> type(ival)

Traceback (most recent call last):
  File "<pyshell#92>", line 1, in <module>
    type(ival)
NameError: name 'ival' is not defined
>>> type(sval)
<type 'str'>
>>> inp=input('Europe floor')
Europe floor

Traceback (most recent call last):
  File "<pyshell#94>", line 1, in <module>
    inp=input('Europe floor')
  File "<string>", line 0
    
    ^
SyntaxError: unexpected EOF while parsing
>>> usf=int(inp)+1

Traceback (most recent call last):
  File "<pyshell#95>", line 1, in <module>
    usf=int(inp)+1
NameError: name 'inp' is not defined
>>> dgr_yyymmdd.py

Traceback (most recent call last):
  File "<pyshell#96>", line 1, in <module>
    dgr_yyymmdd.py
NameError: name 'dgr_yyymmdd' is not defined
>>> pwd

Traceback (most recent call last):
  File "<pyshell#97>", line 1, in <module>
    pwd
NameError: name 'pwd' is not defined
>>> ls-l

Traceback (most recent call last):
  File "<pyshell#98>", line 1, in <module>
    ls-l
NameError: name 'ls' is not defined
>>> a = input("ievadi veselu skaitli")
ievadi veselu skaitli 5 
>>> type(a)
<type 'int'>
>>> a = input("ievadi realu skaitli")
ievadi realu skaitli 3,5
>>> type(a)
<type 'tuple'>
>>> a = input("ievadi realu skaitli")
ievadi realu skaitli 3.5
>>> type(a)
<type 'float'>
>>> a = input ("Who am i")
Who am i student

Traceback (most recent call last):
  File "<pyshell#105>", line 1, in <module>
    a = input ("Who am i")
  File "<string>", line 1, in <module>
NameError: name 'student' is not defined
>>> 
