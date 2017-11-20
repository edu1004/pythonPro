#!/usr/bin/env python 
# -*- coding: utf-8 -*-
#comment 한글
import os

print("os path")

os.system("pwd")
os.system("ls -l")

print("\n")
#=========================

result = os.path.exists("/home/pi/pythonPro")
print("os.path.exists:",result)

print("\n")
#=========================

result = os.path.dirname("/home/pi/pythonPro")
print("os.path.dirname:",result)
result = os.path.dirname("/home/pi")
print("os.path.dirname:",result)


print("\n")
#=========================

result = os.path.isfile("/home/pi/pythonPro/test20classExtends.py")
print("os.path.isfile:",result)

result = os.path.isfile("/home/pi/pythonPro")
print("os.path.isfile:",result)

print("\n")
#=========================

result = os.path.getsize("/home/pi/pythonPro/test20classExtends.py")
print("os.path.getsize:",result)

result = os.path.getsize("/home/pi/pythonPro")
print("os.path.getsize:",result)

print("\n")
#=========================
#doc web site address 
#>>> http://docs.python.org/3/library/os.path.html
