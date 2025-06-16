#!/bin/python3

import sys
import re

if len(sys.argv) < 2:
	print("none")
	exit()


for argument in sys.argv:
	if argument != sys.argv[0]:
		match re.search("ism$", argument):
			case None:
				print(argument + "ism")
