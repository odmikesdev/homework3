#!/usr/bin/env python3

print('Programm calculator')
print('Please enter 2 numbers: ')
try:
	num1 = float(input('Please enter number one: '))
	num2 = float(input('Please enter number two: '))
except ValueError:
	print('Value is incorrect')

action = input('Please enter action *, /, + or -: ')
try:
	if action != '+' and action != '-' and action != '/' and action != '*':
		raise ValueError
	elif action == '+':
		print(f'Result is {num1+num2}')
	elif action == '-':
		print(f'Result is {num1-num2}')
	elif action == '*':
		print(f'Result is {num1*num2}')
	elif action == '/':
		print(f'Result is {num1/num2}')

except ValueError:
	print('Symbol for operation is incorrect')
except ZeroDivisionError:
	print('Can\'t divide by zero')
