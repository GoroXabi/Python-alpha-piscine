#!/bin/python3

o_array = [2, 8, 9, 48, 8, 8, 22, -12, 2]

n_array = set()

for n in o_array:
	if n > 5:
		n_array.add(n+2)
	
print("Original array:", o_array)
print("New array:", n_array)