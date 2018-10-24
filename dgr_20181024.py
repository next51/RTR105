Python 2.7.12 (default, Dec  4 2017, 14:50:18) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> n = 5
>>> while n >0:
	print(n)
	n = n-1
	print('Blastoff!')
	print(n)

	
5
Blastoff!
4
4
Blastoff!
3
3
Blastoff!
2
2
Blastoff!
1
1
Blastoff!
0
>>> while True:
	line = input('>')
	if line == 'done':
		break
	print(line)
	print('Done')

	
>

Traceback (most recent call last):
  File "<pyshell#13>", line 2, in <module>
    line = input('>')
  File "<string>", line 0
    
    ^
SyntaxError: unexpected EOF while parsing
>>> while True:
	line = input('>')
	if line == 'done':
		break
	print(line)
	print('Done!')

	
>

Traceback (most recent call last):
  File "<pyshell#22>", line 2, in <module>
    line = input('>')
  File "<string>", line 0
    
    ^
SyntaxError: unexpected EOF while parsing
>>> while True:
	line = input('>')
	if line == 'done':
		break
	print(line)
	print('Done!')

	
>hello there

Traceback (most recent call last):
  File "<pyshell#24>", line 2, in <module>
    line = input('>')
  File "<string>", line 1
    hello there
              ^
SyntaxError: unexpected EOF while parsing
>>> while True:
	line = input('>')
	if line == 'done':
		break
	print(line)
	print('Done!')

	
>done

Traceback (most recent call last):
  File "<pyshell#26>", line 2, in <module>
    line = input('>')
  File "<string>", line 1, in <module>
NameError: name 'done' is not defined
>>> while True:
    line = input('> ')
    if line[0] == '#':
        continue
    if line == 'done':
        break
    print(line)
    print('Done!')

    
> hello there

Traceback (most recent call last):
  File "<pyshell#28>", line 2, in <module>
    line = input('> ')
  File "<string>", line 1
    hello there
              ^
SyntaxError: unexpected EOF while parsing
>>> while True:
    line = input('> ')
    if line[0] == '#':
        continue
    if line == 'done':
        break
    print(line)
    print('Done!')

    
> 

Traceback (most recent call last):
  File "<pyshell#30>", line 2, in <module>
    line = input('> ')
  File "<string>", line 0
    
    ^
SyntaxError: unexpected EOF while parsing
>>> while True:
    line = input('> ')
    if line[0] == '#':
        continue
    if line == 'done':
        break
    print(line)
    print('Done!')

    
> Done

Traceback (most recent call last):
  File "<pyshell#32>", line 2, in <module>
    line = input('> ')
  File "<string>", line 1, in <module>
NameError: name 'Done' is not defined
>>> print i in[5,4,3,2,1]:
	
SyntaxError: invalid syntax
>>> print i in[5,4,3,2,1] :
	
SyntaxError: invalid syntax
>>> print i in[5,4,3,2,1]:
	
SyntaxError: invalid syntax
>>> print i in[5,4,3,2,1]

Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    print i in[5,4,3,2,1]
NameError: name 'i' is not defined
>>> while True:
    line = input('> ')
    if line[0] == '#':
        continue
    if line == 'done':
        break
    print(line)
print('Done!')while True:
    line = input('> ')
    if line[0] == '#':
        continue
    if line == 'done':
        break
    print(line)
print('Done!')while True:
    line = input('> ')
    if line[0] == '#':
        continue
    if line == 'done':
        break
    print(line)
print('Done!')
SyntaxError: invalid syntax
>>> while True:
    line = input('> ')
    if line[0] == '#':
        continue
    if line == 'done':
        break
    print(line)
    print('done')

    
> yo

Traceback (most recent call last):
  File "<pyshell#40>", line 2, in <module>
    line = input('> ')
  File "<string>", line 1, in <module>
NameError: name 'yo' is not defined
>>> while True:
    line = input('> ')
    if line[0] == '#':
        continue
    if line == 'done':
        break
    print(line)
    print('done')

    
> 'yo'
yo
done
> 

Traceback (most recent call last):
  File "<pyshell#42>", line 2, in <module>
    line = input('> ')
  File "<string>", line 0
    
    ^
SyntaxError: unexpected EOF while parsing
>>> while True:
	line = input('> hello there')
	if line[0] ==
	
SyntaxError: invalid syntax
>>> while True:
	line = input('> hello there')
	if line[0] =='# don't print this'
	
SyntaxError: invalid syntax
>>> while True:
    line = input('> ')
    if line[0] == '#':
        continue
    if line == 'done':
        break
    print(line)
    print('done')

    
> 

Traceback (most recent call last):
  File "<pyshell#48>", line 2, in <module>
    line = input('> ')
  File "<string>", line 0
    
    ^
SyntaxError: unexpected EOF while parsing
>>> 
>>> while True:
    line = input('> ')
    if line[0] == '#':
        continue
    if line == 'done':
        break
    print(line)
    print('done')

    
> '> hello there'
> hello there
done
> 'done'
>>> for i in [5, 4, 3, 2, 1]:
	print(i)
	print('Blastoff')

	
5
Blastoff
4
Blastoff
3
Blastoff
2
Blastoff
1
Blastoff
>>> while True:
	line = raw_input('> ')
	if line[0] == '#':
		continue
	if line 'done':
		
SyntaxError: invalid syntax
>>> while True:
	line = raw_input('> ')
	if line[0] == '#':
		continue
	if line 'done' :
		
SyntaxError: invalid syntax
>>> while True:
	line = raw_input('> ')
	if line[0] == '#':
		continue
	if line 'done':
		
SyntaxError: invalid syntax
>>> while True:
	line = raw_input('> ')
	if line[0] == '#':
		continue
	if line 'done ':
		
SyntaxError: invalid syntax
>>> while True:
	line = raw_input('> ')
	if line[0] == '#':
		continue
	if line ' done ':
		
SyntaxError: invalid syntax
>>> while True:
	line = raw_input('> ')
	if line[0] == '#':
		continue
	if line == 'done':
		break
	print(line)
	print('Done!')

	
> hello there
hello there
Done!
> Done!
Done!
Done!
> done
>>> friends = ['Joseph', 'Glenn', 'Sally']
>>> for friend in friends:
	print('Happy New Year:',friend)
	print('Done!')

	
('Happy New Year:', 'Joseph')
Done!
('Happy New Year:', 'Glenn')
Done!
('Happy New Year:', 'Sally')
Done!
>>> print('Before')
Before
>>> for thing in [9,41,12,3,74,15]:
	print(thing)
	print('After')

	
9
After
41
After
12
After
3
After
74
After
15
After
>>> largest_so_far = -1
>>> print('Before',largest_so_far)
('Before', -1)
>>> for the_num in [9,41,12,3,74,15]:
	if the_num > largest_so_far:
		largest_so_far = the_num
		print(largest_so_far,the_num)
		print('After',largest_so_far)

		
(9, 9)
('After', 9)
(41, 41)
('After', 41)
(74, 74)
('After', 74)
>>> zork = 0
>>> print('Before', zork)
('Before', 0)
>>> for thing in [9,41,12,3,74,15]:
	zork = zork + 1
	print(zork,thing)
	print('After', zork)

	
(1, 9)
('After', 1)
(2, 41)
('After', 2)
(3, 12)
('After', 3)
(4, 3)
('After', 4)
(5, 74)
('After', 5)
(6, 15)
('After', 6)
>>> zork = 0
>>> print('Before',zork)
('Before', 0)
>>> for thing in [9,41,12,3,74,15]:
	zork = zork + thing
	print(zork,thing)
	print('After
	      
SyntaxError: EOL while scanning string literal
>>> for thing in [9,41,12,3,74,15]:
	zork = zork + thing
	print(zork,thing)
	print('After',zork)

	
(9, 9)
('After', 9)
(50, 41)
('After', 50)
(62, 12)
('After', 62)
(65, 3)
('After', 65)
(139, 74)
('After', 139)
(154, 15)
('After', 154)
>>> count = 0
>>> sum = 0
>>> print('Before',count,sum)
('Before', 0, 0)
>>> for value in [9,41,12,3,74,15]:
	count = count + 1
	sum = sum + value
	print(count,sum,value)
	print('After',count,sum,value)

	
(1, 9, 9)
('After', 1, 9, 9)
(2, 50, 41)
('After', 2, 50, 41)
(3, 62, 12)
('After', 3, 62, 12)
(4, 65, 3)
('After', 4, 65, 3)
(5, 139, 74)
('After', 5, 139, 74)
(6, 154, 15)
('After', 6, 154, 15)
>>> print('Before')
Before
>>> for value in [9,41,12,3,74,15]:
	if value > 20
	
SyntaxError: invalid syntax
>>> for value in [9,41,12,3,74,15]:
	if value > 20:
		print('Large number',value)
		print('After')

		
('Large number', 41)
After
('Large number', 74)
After
>>> found = False
>>> print('Before',found)
('Before', False)
>>> for value in [9,41,12,3,74,15]:
	if value == 3:
		found = True
		print(found, value)
		print ('After', found)

		
(True, 3)
('After', True)
