#!/bin/python3

first_num = int(input("Give me the first number: "))
second_num = int(input("Give me the second number: "))
print("Thank you!")
print(f"{first_num} + {second_num} = {first_num + second_num}")
print(f"{first_num} - {second_num} = {first_num - second_num}")
print(f"{first_num} * {second_num} = {first_num * second_num}")
if second_num == 0:
	print("u cant divide by 0.")
else:
	print(f"{first_num} / {second_num} = {first_num / second_num}")