#!/bin/python3

print("Enter a number less than 25")
num = int(input())

if num > 25:
	print("Error")
	quit()
while num <= 25:
	print("Inside the loop, my variable is", num)
	num+=1
