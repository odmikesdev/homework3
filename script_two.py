#!/usr/bin/env python3

print("please enter 2 digit:")
try:
	num1 = float(input('Please enter a number: '))
	num2 = float(input('Please enter a number: '))

	if num1 > num2:
		print(f'Number one is biggest. Number one = {num1}')
	elif num1 == num2:
		print('The numbers are equal')
	else:
		print(f'Number two is biggest. Number two = {num2}')

except ValueError:
	print('Value is incorrect')