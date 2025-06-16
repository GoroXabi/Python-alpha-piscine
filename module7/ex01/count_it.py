#!/bin/python3

import sys

if len(sys.argv) < 2:
	print("none")
	exit()

print("parameters:", len(sys.argv) - 1)

for argument in sys.argv:
	print(f"{argument}:", len(argument))