#!/bin/python3

import sys

def downcase_it(string):
	return string.lower()

if len(sys.argv) < 2:
	print("none")
	quit()

for argument in sys.argv:
	if argument != sys.argv[0]:
		print(downcase_it(argument))
