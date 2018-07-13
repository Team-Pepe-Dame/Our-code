Python 3.5.3 (default, Jan 19 2017, 14:11:04) 
[GCC 6.3.0 20170124] on linux
Type "copyright", "credits" or "license()" for more information.
>>> def is_even():
    numbers = [1, 56, 234, 87, 4, 76, 24, 69, 90, 135]
    from numbers return even numbers
    print(is_even)
    
SyntaxError: invalid syntax
>>> is_even()
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    is_even()
NameError: name 'is_even' is not defined
>>> def is_even():
    is_even = [1, 56, 234, 87, 4, 76, 24, 69, 90, 135]

    
>>> def is_even():
    is_even = [1, 56, 234, 87, 4, 76, 24, 69, 90, 135]

    even_numbers = list(filter(lambda x: x % 2, is_even)
                        print(even_numbers)
			
SyntaxError: invalid syntax
>>> is_even = [1, 56, 234, 87, 4, 76, 24, 69, 90, 135]
>>> even_numbers = list(filter(lambda x: x % 2, is_even)
                        print(even_numbers)
		    
SyntaxError: invalid syntax
>>> is_even = [1, 56, 234, 87, 4, 76, 24, 69, 90, 135]
>>> even_numbers = list(filter(lambda x: x % 2, is_even))
>>> print(even_numbers)
[1, 87, 69, 135]
>>> is_even = [1, 56, 234, 87, 4, 76, 24, 69, 90, 135]
>>> even_numbers = list(filter(lambda x: x % 2 == 0, is_even))
>>> print(even_numbers)
[56, 234, 4, 76, 24, 90]
>>> def is_even(x): return (x: x % 2)
    even = [1, 56, 234, 87, 4, 76, 24, 69, 90, 135]
    list(filter(is_even, even))
    
SyntaxError: invalid syntax
>>> def is_even(x): return (x % 2 == 0)
    even = [1, 56, 234, 87, 4, 76, 24, 69, 90, 135]
    list(filter(is_even, even))
    
SyntaxError: unexpected indent
>>> def is_even(x): return (x % 2 == 0)
	even =[1, 56, 234, 87, 4, 76, 24, 69, 90, 135]
	
SyntaxError: unexpected indent
>>> 
================ RESTART: /home/pi/Python_files/ad_python.py ================
>>> is_even(x)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    is_even(x)
NameError: name 'x' is not defined
>>> 
================ RESTART: /home/pi/Python_files/ad_python.py ================
Traceback (most recent call last):
  File "/home/pi/Python_files/ad_python.py", line 16, in <module>
    list(filter(is_even, even))
TypeError: is_even() takes 0 positional arguments but 1 was given
>>> 
================ RESTART: /home/pi/Python_files/ad_python.py ================
>>> is_even(even)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    is_even(even)
  File "/home/pi/Python_files/ad_python.py", line 14, in is_even
    def is_even(even): return (even % 2 == 0)
TypeError: unsupported operand type(s) for %: 'list' and 'int'
>>> 
================ RESTART: /home/pi/Python_files/ad_python.py ================
[56, 234, 4, 76, 24, 90]
>>> 
================ RESTART: /home/pi/Python_files/ad_python.py ================
[34, 56]
>>> 
================ RESTART: /home/pi/Python_files/ad_python.py ================
[1, 87, 69, 135]
>>> 
================ RESTART: /home/pi/Python_files/ad_python.py ================
>>> odd_numbers(x)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    odd_numbers(x)
NameError: name 'x' is not defined
>>> 
================ RESTART: /home/pi/Python_files/ad_python.py ================
Traceback (most recent call last):
  File "/home/pi/Python_files/ad_python.py", line 34, in <module>
    odd = list(filter(lambda x: x % 2))
TypeError: filter expected 2 arguments, got 1
>>> 
================ RESTART: /home/pi/Python_files/ad_python.py ================
[1, 87, 69, 135]
>>> 
