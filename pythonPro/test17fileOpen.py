#!/usr/bin/env python 
# -*- coding: utf-8 -*-
#comment 한글

print("file open")

#read >> r
f = open("test17.txt","r")
while True:
	data = f.readline()
	if not data: 
		break
	print(data)
#===================

print("\n")
x =10
y = "kim"
print("%d %s \n" %(x,y))

fw = open("test17fw.txt","w")
names = ['aaa','bbb','ccc','ddd','eee']
for i in range(len(names)):
	data = "%d %s \n" %(i ,names[i])
	fw.write(data)
#===================
fw = open("test17fw.txt","r")
lst = fw.readlines()
print(type(lst))
for data in lst:
	print(data)
#===================
fw = open("test17fw.txt","r")
lst = fw.read()
print(type(lst))
for data in lst:
	print(data)
#===================



#===================
f.close()
fw.close()
