#!/bin/python3

import sys
import re

if len(sys.argv) < 3:
	print("none")
	quit()

print(len(re.findall(sys.argv[1], sys.argv[2])))