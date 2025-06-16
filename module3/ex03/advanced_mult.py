#!/bin/python3


base = int(0)
num = int(0)

while base <= 10:
	print(f"Table of {base}:", end=' ')
	while num <= 10:
		print(num * base, end=' ')
		num += 1
	print("")
	num = 0
	base += 1