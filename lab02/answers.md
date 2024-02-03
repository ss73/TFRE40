# Answers to lab 02

## Task 1
> Create a new Python file by right-clicking on the lab02 directory and selecting New File.
> Name the file hello.py and enter the following classic program code into the file:
>
> `print('hello world')`


The file is available here: [hello.py](hello.py)

## Task 2
> Run the Python file by clicking on the triangle ( ▷ ) at the top right in VS Code. When the file
>runs, the text "hello world" will be printed in the terminal

```python
$ /bin/python3 ~/TFRE40/lab02/hello.py
hello world
```

## Task 3
> If you manage to run the program, proceed to subtask 4


## Task 4
>This program is a very simple calculator that reads two floating-point numbers from the user and displays their sum.

```python
print('Enter two numbers:')
x1 = float(input())
x2 = float(input())
print(x1, '+', x2, '=', x1+x2)
```

### Subtask A
>Write this program into a new Python file (e.g., named `calculator.py`) in the `lab02` directory. Test the program by running it and entering various numbers.

The [`calculator.py`](calculator.py) program generates the following output:

```python
Enter two numbers:
42
7
42.0 + 7.0 = 49.0
```

### Subtask B
> Some floating-point numbers cannot be represented with absolute accuracy, for example, the number 0.1. This is due to how floating-point numbers are represented internally in computers. Test entering 0.1 and 0.2 and see what the result is.

```python
Enter two numbers:
0.1
0.2
0.1 + 0.2 = 0.30000000000000004
```

### Subtask C
>The input function reads a line, and the program converts the entire line to a floating-point number. Test entering two numbers on the same line. What goes wrong?

```python
Enter two numbers:
1 2
Traceback (most recent call last):
  File "~/TFRE40/lab02/calculator.py", line 2, in <module>
    x1 = float(input()) 
ValueError: could not convert string to float: '1 2'
```

*Comment*: Since there is a space between the numbers, the float function is not able to parse the input. The function expects all characters to be numeric or a "well formed" numeric expression, e.g. `-42.01E42`.

### Subtask D
> Expand the program with more operations, including subtraction, multiplication, and
> division. The output for the other operations should be similar to the addition output.

The extended calculator is implemented in the same source file,
[calculator.py](calculator.py)

```python
print('Enter two numbers and an operator (+, -, *, /):')
x1 = float(input()) 
x2 = float(input())
op = input().strip()
if op == '+':
    print(x1, '+', x2, '=', x1+x2)
elif op == '-':
    print(x1, '-', x2, '=', x1-x2)
elif op == '*':
    print(x1, '*', x2, '=', x1*x2)
elif op == '/':
    print(x1, '/', x2, '=', x1/x2)
else:
    print('Unknown operation:', op)


```

## Task 5
> We will now implement our own functions and call them.
>
> The hypotenuse function will be used as an example:

```python
def hypotenuse(a, b):
c = math.sqrt(a**2 + b**2)
return c
```

### Subtask A
> Enter the program code (both the function and the function call) in a new Python file.

The source code is available here: [`pythagoras.py`](pythagoras.py)

When running the program, the following output is produced:
```
In a right triangle with sides 5, 10; calculate the hypothenuse
The hypotenuse is 11.180339887498949
```

### Subtask B
> Test printing the value of one of the parameters after calling hypotenuse, i.e., outside the function. What error do you encounter? Similarly, local variables work for a function. Perform a similar test for the local variable c and print its value after the function call.


When running the statement `print(a)`:

```python
Traceback (most recent call last):
  File "pythagoras.py", line 9, in <module>
    print(a)
NameError: name 'a' is not defined
```

The same result (i.e. `NameError`) is output when referencing local variables outside of their scope with `print(c)`

### Subtask C
>The above call uses 5 and 10 as side lengths. Modify the program (except for the
>hypotenuse function) to read the side lengths as numbers from the user.

The relevant part of the [`code`](pythagoras.py) is defined by the following code block:
```python
def get_sides_from_user():
    print('Input first side length:')
    a = float(input())
    print('Input second side length:')
    b = float(input())
    return a,b

print('Calculating hypotenuse in a right triangle')
print('Hypotenuse is:', hypotenuse(*get_sides_from_user()))
```

### Subtask D
> You can use the Pythagorean theorem to calculate the distance between two points
> (x1 , y1 ) and (x2 , y2 ) using sqrt((x2 − x1)^2 + (y2 − y1)^2). Implement a new function `distance` with four parameters (`x1`, `y1`, `x2`, `y2`) that calculates the distance between two points. The function should use the hypotenuse function.

The relevant part of the [`source code`](pythagoras.py) is covered by the following code block:

```python
def distance(x1, y1, x2, y2):
    return hypotenuse(x2-x1, y2-y1)
```

### Subtask E
>Read the coordinates for two points (4 numbers) from the user and print the distance between them.

The relevant part of the [`source code`](pythagoras.py) is contained in the following code block:

```python
def get_points_from_user():
    print("Input first point's x-value:")
    x1 = float(input())
    print("Input first point's y-value:")
    y1 = float(input())
    print("Input second point's x-value:")
    x2 = float(input())
    print("Input secod point's y-value:")
    y2 = float(input())
    return x1, y1, x2, y2

print('Calculating the distance between two points in Euclidian space')
print('Distance is:', distance(*get_points_from_user()))
```

## Task 6
>We will now implement some of the formulas we saw in Exercise 1 as functions. Implement the following functions (and the rest of the exercise) in a new file `functions.py`:
> 
> * to_km: converts miles to kilometers
> * to_fahrenheit: converts degrees Celsius to Fahrenheit
> * to_celsius: converts degrees Fahrenheit to Celsius
> * circle_area: calculates the area of a circle given its diameter
> 
> &nbsp;

The following is added to the [`functions.py`](functions.py) program

```python
def to_km(miles):
    return round(1609.344 * miles / 1000, 3)

def to_fahrenheit(celsius):
    return round((9/5)*celsius + 32, 2)

def to_celsius(fahrenheit):
    return round((5/9)*(fahrenheit-32), 2)

def circle_area(diameter):
    return math.pi * diameter * diameter / 4
```

When the program is run, the following output is produced:

```
Unit conversions and circle area formula
5 miles in km: 8.047
25 deg. C in F: 77.0
100 deg. F in C: 37.78
Area of circle with diameter 5: 19.63
```

## Task 7
> Implement the `print_c2f_table` function, which prints all degrees Celsius within a specific range along with their corresponding degrees in Fahrenheit. The range is determined by two parameters to the function

The function is implemented in the same source file, [`functions.py`](functions.py).

```python
def print_c2f_table(first, last):
    for c in range(first, last+1):
        print(c, to_fahrenheit(c))
```

When run, the arguments `3` and `5` are passed, producing the following output:

```
Celsius to Fahrenheit 3-5
3 37.4
4 39.2
5 41.0
```

## Task 8
> Implement the print_odd_numbers function, which prints all odd integers within a specified range, determined by two parameters.

The function is implemented in the same source file, [`functions.py`](functions.py). The relevant part is the following:

```python
def print_odd_numbers(first, last):
    for n in range(first, last+1):
        print(n, end=' ') if n % 2 == 1 else None
    print()

print('\nOdd numbers 2-11')
print_odd_numbers(2,11)
```

When run, the following output is produced:

```
Odd numbers 2-11
3 5 7 9 11
```
