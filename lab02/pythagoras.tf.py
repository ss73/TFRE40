import math

def hypotenuse(a, b):
    c = math.sqrt(a**2 + b**2)
    return c

def distance(p1x,p1y,p2x,p2y):
    return hypotenuse(p1x-p2x,p1y-p2y)

# print('Enter the lengths of the two sides:')
# first = float(input())
# second = float(input())
# print('The hypotenuse is', hypotenuse(first, second))
# print(a)
# print(c)


print('Enter the the coordinates of point A (x y):')
x1,y1 = map(int, input().split())
print('Enter the the coordinates of point B (x y):')
x2,y2 = map(int, input().split())

print('The distance between A and B is ', distance (x1,y1,x2,y2))
