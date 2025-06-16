#!/bin/python3

import sys

if len(sys.argv):
	print("none")

for argument in sys.argv:
	if argument.isdigit() == False and argument != sys.argv[0]:
		print(argument)
		break