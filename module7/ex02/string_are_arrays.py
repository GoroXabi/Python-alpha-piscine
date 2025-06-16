#!/bin/python3

import sys
import re

if len(sys.argv) != 2:
	print("none")
	exit()

string = sys.argv[1]

for c in string:
	if c == 'z':
		print(c, end='')


if len(re.findall('z', string)) == 0:
	print("none")
else:
	print('')