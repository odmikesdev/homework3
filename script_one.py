#!/usr/bin/env python3

print('Program for converting a number to a day of the week:')
try:
	weekdays = int(input('Please enter a number between 1 and 7: '))

	if weekdays == 1:
		print('This is Monday')
	elif weekdays == 2:
		print('This is Tuesday')
	elif weekdays == 3:
		print('This is Wednesday')
	elif weekdays == 4:
		print('This is Thursday')
	elif weekdays == 5:
		print('This is Friday')
	elif weekdays == 6:
		print('This is Saturday')
	elif weekdays == 7:
		print('This is Sunday')
	else:
		raise ValueError

except ValueError:
	print('The entered value is not correct, please enter a number between 1 and 7')