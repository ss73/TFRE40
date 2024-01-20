import math

skip_input = True

def hypotenuse(a, b):
    c = math.sqrt(a**2 + b**2)
    return c

def distance(x1, y1, x2, y2):
    return hypotenuse(x2-x1, y2-y1)

print('In a right angle with sides 5, 10; calculate the hypotenuse')
print('The hypotenuse is', hypotenuse(5, 10))

# Referencing function parameters outside of the fuction:
#
# print(a)
#
# Traceback (most recent call last):
#   File "pythagoras.py", line 9, in <module>
#     print(a)
# NameError: name 'a' is not defined
#
#
# Referencing local variables outside of their scope:
#
# print(c)
#
# Produces the same result (NameError)

def get_sides_from_user():
    print('Input first side length:')
    a = float(input())
    print('Input second side length:')
    b = float(input())
    return a,b

if not skip_input:
    print('Calculating hypotenuse in a right triangle')
    print('Hypotenuse is:', hypotenuse(*get_sides_from_user()))

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

if not skip_input:
    print('Calculating the distance between two points in Euclidian space')
    print('Distance is:', distance(*get_points_from_user()))


