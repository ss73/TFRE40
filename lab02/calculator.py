# Task 4

print('Enter two numbers:')
x1 = float(input())
x2 = float(input())
print(x1, '+', x2, '=', x1+x2)

# Base 2 representation of numbers have some quirks:
# 
# Enter two numbers:
# 0.1
# 0.2
# 0.1 + 0.2 = 0.30000000000000004

# Entering two numbers in the same line:
#
# Enter two numbers:
# 1 2
# Traceback (most recent call last):
#   File "/home/stellan/src/py/TFRE40/lab02/calculator.py", line 2, in <module>
#     x1 = float(input()) 
# ValueError: could not convert string to float: '1 2'



print('Press Return to continue')
input()

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

