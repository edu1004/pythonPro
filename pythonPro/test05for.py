#!/usr/bin/env python 
# -*- coding: utf-8 -*-
#comment 한글
import sys

print('for')

#list >> java,c : array
lst = [11,22,33,44,55]
sum = 0

for i in lst:
	print(i)
	sum += i
print("sum:",sum)
print("=======")

for i in range(10):
	print(i),
#, 가로출력
print
for i in range(len(lst)):
	print(i),
	print(lst[i])

#10~19
for i in range(10,20):
#python 2.x
	print("{}*{}={}".format(i,10,i*10)),
#	python3 >> print(i,end=',')
#	print(i,'*',3,'=',i*3,end=' ')	
#9*9dan






