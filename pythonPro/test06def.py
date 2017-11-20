#!/usr/bin/env python 
# -*- coding: utf-8 -*-
#comment 한글

#function
print('def')

def sum(a,b):
	print("sum(a,b)>>>a:{},b:{}".format(a,b))

sum(10,20)

def sum():
	print("sum()")
sum()

def sum(x,y):
	return x+y

sumXY = sum(100,200)
print("sumXY",sumXY)

def test(a,b,c,d,e):
	lst = [a,b,c,d,e,"kim"]
	for item in lst:
		print(item),
test(1,2,3,4,5)

def test2(*args):
	for item in args:
		print(item),
print("\n")
test2(11,22,33,44,55,66,77,"yangssem")
print("\n")
def getInputName():
	name = raw_input("input name:")
#	name = input("input name:")
	return name

print(getInputName())	
	
print("\n")

def printList(lst):
	for item in lst:
		print(item),

printList([77,88,99])



