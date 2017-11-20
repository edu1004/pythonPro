#!/usr/bin/env python 
# -*- coding: utf-8 -*-
#comment 한글

print("tuple")

#list read create update delete OK
lst = []
lst = [0,0,0,0]
lst = [1,2,3,4]
#===================

#tuple read only
tp = ()
tp = (0,0,0,0)
tp = (1,2,3,4)
tp = (22,33)
tp = (1,2,(3,4,5))
#===================
print(type(tp))

for item in tp:
	print(item)
print("\n")
#===================
#del tp[0]
#tp[0] = 100
#tp[1:2] = (77,88)
tp = tp + (555,666)
tp = tp * 2
for item in tp:
	print(item)
print("\n")

#===================
tp = (1,2,3,('aaa','bbb'))
tp = tp[1:]
for item in tp:
	print(item)
print("\n")

#===================
tp = (1,2,3,('aaa','bbb'))
tp = tp[3:]
for item in tp:
	print(item)
print("\n")



