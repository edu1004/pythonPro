#!/usr/bin/env python 
# -*- coding: utf-8 -*-
#comment 한글

print("extends")

class Person:
	pname = "kim"
	def __init__(self):
		print("Person__init__")
	def getPname(self):
		return self.pname
	def getSum(self,x,y):
		return x+y

p = Person()
print(p.pname)
print(p.getPname())
print("\n")
#=========================

class Students(Person):
	sname = "LEE"
	def __init__(self):
		print("Students__init__")
	def getSname(self):
		return self.sname
		
	def getSum(self,x,y):
		return (x+y)*2
	

s = Students()
print(s.sname)
print(s.getSname())
print("\n")
#=========================

print(Person.__bases__)
print(Students.__bases__)

print("\n")
#=========================

print(issubclass(Students,Person))
print(issubclass(Person,Students))


print("\n")
#=========================

print(s.pname)
print(s.getPname())
print(p.getSum(10,20))
print(s.getSum(100,200))

print("\n")
#=========================
