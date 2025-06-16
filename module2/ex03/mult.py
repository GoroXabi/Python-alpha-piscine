#!/bin/python3

print("Enter the first number:")
first_num = int(input())
print("Enter the second number:")
second_num = int(input())

res_num = first_num * second_num

print(f"{first_num} x {second_num} = {res_num}")

if res_num < 0:
	print("The result is negative.")
if res_num > 0:
	print("The result is positive.")
if res_num == 0:
	print("The result is positive and negative.")