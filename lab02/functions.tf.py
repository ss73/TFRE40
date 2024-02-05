import math

print('*** Uppgift 6 ***')

def to_km(miles):
    return 1.609344 * miles

print('25 miles equals',to_km(25), 'km.')


def to_farenheit(celcius):
    return (9/5)*celcius + 32

def to_celcius(farenheit):
    return (5/9)*(farenheit-32)

print('37 degrees Celcius converted to Farenheit and back:', to_celcius(to_farenheit(37)) )


def circle_area(diameter):
    return math.pi * diameter ** 2 / 4

print('A circle with diameter 1 has the area', circle_area(1))



print('*** Uppgift 7 ***')

def print_c2f_table(start,stop):
    for c in range(start,stop+1):
        print(c, to_farenheit(c))

print_c2f_table(3,5)



print('*** Uppgift 8 ***')

def odd(number):
    return (number % 2)

def print_odd_numbers(start,stop):
    for num in range(start,stop+1):
        if odd(num): print (num)

print('0..20')
print_odd_numbers(0,20)

print('131..143')
print_odd_numbers(131,143)
