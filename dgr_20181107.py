Python 2.7.12 (default, Dec  4 2017, 14:50:18) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> fhand = open('mbox.txt')
>>> print(fhand)
<open file 'mbox.txt', mode 'r' at 0x7f374afb88a0>
>>> fhand = open('mbox.txt')
>>> count = 0
>>> for line in fhand:
	count = count + 1
	print('Line Count:', count)

	
('Line Count:', 1)
('Line Count:', 2)
>>> stuff = 'Hello
SyntaxError: EOL while scanning string literal
>>> stuff = 'Hello
SyntaxError: EOL while scanning string literal
>>> stuff = 'Hello\nWorld!'
>>> stuff
'Hello\nWorld!'
>>> print(stuff)
Hello
World!
>>> stuff = 'X\nY'
>>> print(stuff)
X
Y
>>> len(stuff)
3
>>> fhand = open('mbox-short.txt')
>>> for line in fhand:
	if line.startswith('From:'):
		print(line)

		
From: 

>>> fhand = open('mbox-short.txt')
>>> inp = fhand.read()
>>> print(len(inp))
355
>>> print(inp[:20])
From 
stephen.marqua
>>> print(inp[:300])
From 
stephen.marquard@uct.ac.za
Sat Jan  5 09:14:16 2008
Return
-
Path: <
postmaster@collab.sakaiproject.org
>
Date: Sat, 5 Jan 2008 09:12:18 
-
0500
To: 
source@collab.sakaiproject.org
From: 
stephen.marquard@uct.ac.za
Subject: [
sakai
] 
svn
commit: r39772 
-
content/branches/
Details: http://
so
>>> fhand = open('mbox-short.txt')
>>> for line in fhand:
	line = line.rstrip()
	if line.startswith('From'):
		print(line)

		
From
From:
>>> fhand = open('mbox-short.txt')
>>> for line in fhand:
	line = line.rstrip()
	if not '@uct.ac.za'in line:
		continue
	print(line)

	
stephen.marquard@uct.ac.za
stephen.marquard@uct.ac.za
