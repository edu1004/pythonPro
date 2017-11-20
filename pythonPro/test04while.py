#!/usr/bin/env python 
# -*- coding: utf-8 -*-
#comment 한글
import sys

print('while')

i=0
while True:
	i += 1
	if i==5 : continue
	print(i)
	if i==10: break
	name = raw_input("input name:")
	print("input name is {}".format(name))



