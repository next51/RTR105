Python 2.7.12 (default, Dec  4 2017, 14:50:18) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> x = 5
>>> if x < 10
SyntaxError: invalid syntax
>>> if x < 10:
	print('Smaller')
	if x > 20:
		print('bigger')
		print('finish')

		
Smaller
>>> x = 5
>>> if x==5:
	print('equals 5')
	if x >4:
		print('greater than 6')
		if x<6:print('less than 6')
		if x <= 5:
			print('less than or Equals 5')
			if x !=6:
				print('not equal 6')
				print(x)

				
equals 5
greater than 6
less than 6
less than or Equals 5
not equal 6
5
>>> 
>>> x=5
>>> print('before 5')
before 5
>>> if x ==5:
	print('is 5')
	print('is still 5')
	print('third 5')
	print('afterwards 5')
	if x==6:
		print('is 6')
		print('is still 6')
		print('third 6')
		print('afterwards 6'°
		      
SyntaxError: invalid syntax
>>> if x ==5:
	print('is 5')
	print('is still 5')
	print('third 5')
	print('afterwards 5')
	if x==6:
		print('is 6')
		print('is still 6')
		print('third 6')
		print('afterwards 6')

		
is 5
is still 5
third 5
afterwards 5
>>> x=5
>>> if x>2:
	print('bigger than 2')
	print('still bigger')
	print('done with 2')
	for i>2:
		
SyntaxError: invalid syntax
>>> if x>2:
	print('bigger than 2')
	print('still bigger')
	print('done with 2')
	if i>2:
		print('bigger than 2')
		print('done with i',i)
		print('all done')

		
bigger than 2
still bigger
done with 2

Traceback (most recent call last):
  File "<pyshell#45>", line 5, in <module>
    if i>2:
NameError: name 'i' is not defined
>>> 
>>> x=5
>>> id x>2:
	
SyntaxError: invalid syntax
>>> print('bigger than 2')
bigger than 2
>>> print('still bigger')
still bigger
>>> print('done with 2')
done with 2
>>> for i in range(5):
	print(i)
	if i>2:
		print('bigger than 2')
		print('done wit i',i)
		print('all done')

		
0
1
2
3
bigger than 2
('done wit i', 3)
all done
4
bigger than 2
('done wit i', 4)
all done
>>> x=42
>>> if x>1:
	print('more than one')
	if x<100:
		print('less than 100')
		print('all done')

		
more than one
less than 100
all done
