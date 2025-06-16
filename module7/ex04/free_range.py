#!/bin/python3

import sys
import re

if len(sys.argv) < 3:
	print("none")
	exit()

begin = int(sys.argv[1])
end = int(sys.argv[2])

array = []

for n in range(begin, end + 1):
	array.append(n)

print(array)