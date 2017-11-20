#!/usr/bin/env python 
# -*- coding: utf-8 -*-
#comment 한글
import sys
print("sys")

if len(sys.argv) > 3:
	print("sys.argv[0]",sys.argv[0])
	print("sys.argv[1]",sys.argv[1])
	print("sys.argv[2]",sys.argv[2])
	print("sys.argv[3]",sys.argv[3])

print("input name:")
name = sys.stdin.readline()
print("name:",name)
