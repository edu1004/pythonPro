#!/usr/bin/env python 
# -*- coding: utf-8 -*-
#comment 한글

print("inner def")

print(abs(-11))
print(abs(11))

print("all:",all([]))
print("all:",all([1,2,3]))
print("all:",all([1,2,3,0]))
print("all:",all(['aaa','bbb','ccc']))
print("all:",all(['aaa','bbb','ccc','']))

print("any:",any(['aaa','bbb','ccc','']))
print("any:",any([[],0,'']))

print(chr(97),chr(48),chr(66))

print(dir([1,2,3]))
print(dir((1,2,3)))
print(dir("kim"))

print(divmod(7,3))
print(type(divmod(7,3)))
print(type(divmod(22.3,12.5)))

print(eval("'kim'+'lee'"))
print(eval("11+22"))

print(hex(10),hex(255),hex(0))

a=10
print(id(a))

name="yangssem"
print(id(name))

class Person:
	pname="yangssem"
p = Person()
print(isinstance(p,Person))

#=======================

def fn(item):
	return item >=0

print(list(filter(fn,[0,-1,1,2,-2])))
print(list(filter(lambda item:item >= 0,[0,-1,1,2,-2])))


#=======================

def fn2(item):
	return item **2

print(list(map(fn2,[1,2,3,4,-5])))
print(list(map(lambda item:item**2,[1,2,3,4,-5])))

print(list(zip([1,2,3],[4,5,6])))
print(list(zip([1,2,3],[4,5,6],[100,200,300])))
print(list(zip("abc","123")))
