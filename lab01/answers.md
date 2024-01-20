# Excercise 1-5

To start the Python interpreter, you need a terminal. In VS Code, open a terminal through
the menu *Terminal -> New Terminal*. Then, type python3 in the terminal to start the Python
interpreter. 

This is useful for testing various things or using Python as
a simple calculator.

To exit the Python interpreter, call the `exit()` function.

```python
stellan@minttu:~/tfre40-labs$ python3
Python 3.10.12 (main, Nov 20 2023, 15:14:05) [GCC 11.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> 10 + 2*5
20
>>> exit()
```

# Excercise 6

## Miles to kilometers

The English mile is used as a unit of length in the USA, and one English mile is equal
to `1609.344` meters. How many kilometers are in 5 English miles?
```python
>>> miles2km = lambda miles: round(1609.344 * miles / 1000, 3)
>>> miles2km(5)
8.047
>>> 
```

## Celcius to Fahrenheit

How many degrees Fahrenheit is
25 degrees Celsius? How many degrees Celsius is 100 degrees Fahrenheit?

```python
>>> c2f = lambda c: round((9/5)*c + 32, 2)
>>> f2c = lambda f: round((5/9)*(f-32), 2)
>>> c2f(25)
77.0
>>> f2c(100)
37.78
>>> 
```

## Circle area

What area
do circles with diameters of 5 cm and 10 cm have?

```python
>>> import math
>>> circle_area = lambda d: math.pi * d * d / 4
>>> circle_area(5)
19.634954084936208
>>> circle_area(10)
78.53981633974483
>>> 
```

# Excercise 7-8

Variables a and b are assigned two arbitrary integers. Your task is to swap the values of the variables a and b using assignment statements so
that variable a gets the value of b, and variable b gets the value of a. Your solution must work for
arbitrary values of a and b.

```python
>>> a = 13
>>> b = 105
>>> a, b = b, a
>>> a
105
>>> b
13
>>> a, b = 5, 15
>>> a, b = b, a
>>> a
15
>>> b
5
>>> 
```

# Excercise 9

Investigate what the
value and type are for the following expressions:
* 10
* 10.0
* 'hello'
* a
* math.pi
* 10 - 5
* 10 + 5
* 10 / 5
* 10.0 + 5
* 10.0 / 2
* 10 // 3
* 10.0 // 3
* 'hello' + ' world'
* '10' + '5'
* 'hello' * 8

```python
>>> type(10)
<class 'int'>

>>> type(10.0)
<class 'float'>

>>> type('hello')
<class 'str'>

>>> type(a) #Variable 'a' was defined in Excercise 7-8
<class 'int'>

>>> type(math.pi)
<class 'float'>

>>> type(10-5)
<class 'int'>

>>> type(10-5)
<class 'int'>

>>> type(10+5)
<class 'int'>

>>> type(10/5)
<class 'float'>

>>> type(10.0+5)
<class 'float'>

>>> type(10.0/2)
<class 'float'>

>>> type(10//3)
<class 'int'>

>>> type(10.0//3)
<class 'float'>

>>> type('hello' + 'world')
<class 'str'>

>>> type('10' + '5')
<class 'str'>

>>> type('hello' * 8)
<class 'str'>
>>> 
```

# Excercise 10
Test to provoke the following types of errors:
* Syntax Error 
* Name Error 
* Type Error 
* Division by Zero
```python
>>> 5+*5
  File "<stdin>", line 1
    5+*5
      ^
SyntaxError: invalid syntax

>>> math.pizza
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: module 'math' has no attribute 'pizza'

>>> hello()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'hello' is not defined. Did you mean: 'help'?

>>> '5' + 10
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str

>>> 10/0
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero
>>> 
```

# Excercise 11
Print all the number between 0 and 10, using a for-loop. Afterwards, print all numbers
between 5 and 15.

```python
>>> for i in range(1,11):
...     print(i, end=' ')
... 
1 2 3 4 5 6 7 8 9 10 >>> 
>>> 
>>> for i in range(5,16):
...     print(i, end=' ')
... 
5 6 7 8 9 10 11 12 13 14 15 >>> 

```

# Excercise 12
Look at what happens if you do not indent the statements inside the for-loop. Which error
do you get?

```python
>>> for i in range(1,11):
... print(i, end=' ')
  File "<stdin>", line 2
    print(i, end=' ')
    ^
IndentationError: expected an indented block after 'for' statement on line 1
>>> 

```

# Excercise 13

Using for loops, generate a pattern with lines that  alternates between “*” symbols and “-” symbols. The result should look like this:
```
--------------------
********************
--------------------
********************
--------------------
********************
--------------------
********************
--------------------
********************
```

```python
>>> for row in range(10):
...     for col in range(20):
...         print('-', end='') if row % 2 == 0 else print('*', end='')
...     print()
... 
--------------------
********************
--------------------
********************
--------------------
********************
--------------------
********************
--------------------
********************
>>> 

```

# Excercise 14

modify your code, so that your
loops print a triangular pattern, like the pattern below.

```
-
**
---
****
-----
*****
----
***
--
*
```

```python
>>> for row, count in enumerate([*range(1,6), *range(5,0,-1)]):
...     for col in range(count):
...             print('-', end='') if row % 2 == 0 else print('*', end='')
...     print()
... 
-
**
---
****
-----
*****
----
***
--
*
```

# Excercise 15
Make a cool pattern and show it to your friends.

```python
>>> for row in range(20):
...     for col in range(10-abs(10-row)):
...             print('\N{fire}', end='') if row % 2 == 0 else print('\N{i love you hand sign}', 
end='')
...     print()
... 

🤟
🔥🔥
🤟🤟🤟
🔥🔥🔥🔥
🤟🤟🤟🤟🤟
🔥🔥🔥🔥🔥🔥
🤟🤟🤟🤟🤟🤟🤟
🔥🔥🔥🔥🔥🔥🔥🔥
🤟🤟🤟🤟🤟🤟🤟🤟🤟
🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥
🤟🤟🤟🤟🤟🤟🤟🤟🤟
🔥🔥🔥🔥🔥🔥🔥🔥
🤟🤟🤟🤟🤟🤟🤟
🔥🔥🔥🔥🔥🔥
🤟🤟🤟🤟🤟
🔥🔥🔥🔥
🤟🤟🤟
🔥🔥
🤟
```
