#!/usr/bin/env python 
# -*- coding: utf-8 -*-
#comment 한글

print("list")

lst = []
lst = [0,0,0,0]
lst = [1,2,3,4]
#===================

lst = [0 for _ in range(10)]
print(type(lst))
for item in lst:
	print(item,end=' ')
print("\n")
#===================

lst = [i for i in range(10)]
print(type(lst))
for item in lst:
	print(item,end=' ')
print("\n")

#===================

lst = [i+1 for i in range(10)]
print(type(lst))
for item in lst:
	print(item,end=' ')
print("\n")
#===================

lst = [i**2 for i in range(10)]
print(type(lst))
for item in lst:
	print(item,end=' ')
print("\n")
#===================

lst = [i**2 for i in range(10)]
print(type(lst))
for index,item in enumerate(lst):
	print(index,item,end=',')
print("\n")
#===================
print("lst[-1]:",lst[-1])
print("lst[-2]:",lst[-2])

print("\n")
#===================
lst = [11,22,33]
lst = lst + [44,55,66]

for item in lst:
	print(item)

print("\n")
#===================
lst = lst * 2

for item in lst:
	print(item)

print("\n")
#===================

lst.append(11)
lst.append(22)
lst.append(33)

for item in lst:
	print(item)

print("\n")
#===================
lst.sort()
for item in lst:
	print(item)

print("\n")
#===================
lst.reverse()
for item in lst:
	print(item)

print("\n")
#===================
lst = ['x','c','k']
lst.sort()
for item in lst:
	print(item)

print("\n")
#===================
lst = ['x99','c88','k77','88','k77','c88','77']
lst.sort()
for item in lst:
	print(item)

print("\n")
#===================


lst = ['x99','c88']
lst.insert(0,'aaa')
lst.insert(3,'bbb')
lst.insert(10,'xxx')
lst.insert(7,'sss')
print("len(lst):",len(lst))
for item in lst:
	print(item)

print("\n")
#===================

lst = ['x99','c88','x99']
lst.remove('x99')
print("len(lst):",len(lst))
for item in lst:
	print(item)

print("\n")
#===================

lst = ['x99','c88','x99']
lst.pop()
print("lst.pop():",lst.pop())
print("len(lst):",len(lst))
for item in lst:
	print(item)

print("\n")
#===================

lst = [1,2,3,4,5,6]
#lst[1] = 22

#lst[2] = [77,88,99]
#lst[1:1] = [33,44,55]
#lst[1:2] = [33,44,55]
lst[1:3] = [33,44,55]

print("len(lst):",len(lst))
for item in lst:
	print(item)

print("\n")
#===================
lst = [1,2,3,4,5,6]
del lst[1]

print("len(lst):",len(lst))
for item in lst:
	print(item)

print("\n")
#===================
lst = [1,2,3,4,5,6]
lst[2:4] = []

print("len(lst):",len(lst))
for item in lst:
	print(item)

print("\n")
#===================

lst = [1,2,3,4,5,6]
lst.append([11,22,33])
lst.extend([44,55,66])

print("len(lst):",len(lst))
for item in lst:
	print(item)

print("\n")
#===================


