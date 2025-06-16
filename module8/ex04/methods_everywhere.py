#!/bin/python3

import sys

def shrink(string):
	print(string[0:8])

def enlarge(string):
	print(string + (8 - len(string)) * 'Z')

if len(sys.argv) < 2:
	print("none")
	quit()

for argument in sys.argv:
	if argument != sys.argv[0]:
		if len(argument) > 8:
			shrink(argument)
		if len(argument) < 8:
			enlarge(argument)
		if len(argument) == 8:
			print(argument)
