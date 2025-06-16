#!/bin/python3

import sys

if len(sys.argv) < 3:
	print("none")
	quit()

for argument in reversed(sys.argv):
	if argument.isdigit() == False and argument != sys.argv[0]:
		print(argument)	