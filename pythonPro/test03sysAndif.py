#!/usr/bin/env python 
# -*- coding: utf-8 -*-
#comment 한글
import sys

print('sys and if else')
print('msg:',sys.argv[0])
print('msg:',sys.argv[1])
#python ./test03sysAndif.py 11

print("input name:")
#python 2.x >> raw_input(), python 3.x >> input()
name=raw_input()
hi="hello"

if True :
	print("{},{}".format(hi,name))

if 5>=5 :
	print("big")

a = 3.14
print(type(a))
print(float(a))
print(type(float(a)))

if float(a)==3.14:
	print("lee")
elif a==3:
	print("sam")
elif a==5:
	print("oh")
else :
	print("other")





