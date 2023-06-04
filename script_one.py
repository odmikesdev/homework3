#!/usr/bin/env python3

print('Program for converting a number to a day of the week:')
try:
	weekdays = int(input('Please enter a number between 1 and 7: '))

	if weekdays == 1:
		print('This is Monday')
	if weekdays == 2:
		print('This is Tuesday')
	if weekdays == 3:
		print('This is Wednesday')
	if weekdays == 4:
		print('This is Thursday')
	if weekdays == 5:
		print('This is Friday')
	if weekdays == 6:
		print('This is Saturday')
	if weekdays == 7:
		print('This is Sunday')

except ValueError:
	print('The entered value is not correct, please enter a number between 1 and 7')