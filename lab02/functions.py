# to_km: converts miles to kilometers
# to_fahrenheit: converts degrees Celsius to Fahrenheit
# to_celsius: converts degrees Fahrenheit to Celsius
# circle_area: calculates the area of a circle given its diameter

import math

def to_km(miles):
    return round(1609.344 * miles / 1000, 3)

def to_fahrenheit(celsius):
    return round((9/5)*celsius + 32, 2)

def to_celsius(fahrenheit):
    return round((5/9)*(fahrenheit-32), 2)

def circle_area(diameter):
    return math.pi * diameter * diameter / 4

print('\nUnit conversions and circle area formula')
print('5 miles in km:', to_km(5))
assert to_km(5) == 8.047

print('25 deg. C in F:', to_fahrenheit(25))
assert to_fahrenheit(25) == 77.0

print('100 deg. F in C:', to_celsius(100))
assert to_celsius(100) == 37.78 

print('Area of circle with diameter 5:', round(circle_area(5), 2))
assert circle_area(5) == 19.634954084936208


def print_c2f_table(first, last):
    for c in range(first, last+1):
        print(c, to_fahrenheit(c))

print('\nCelsius to Fahrenheit 3-5')
print_c2f_table(3, 5)

def print_odd_numbers(first, last):
    for n in range(first, last+1):
        print(n, end=' ') if n % 2 == 1 else None
    print()

print('\nOdd numbers 2-11')
print_odd_numbers(2,11)